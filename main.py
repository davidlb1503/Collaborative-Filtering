import pandas as pd
import numpy as np
from scipy.stats import pearsonr

#user-item rating matrix with missing values
data = {
    'The Dark Knight': [5, 4, 3, np.nan, 1, 5, 4, 3, 2, np.nan],
    'Inception': [4, np.nan, 4, 5, 2, 4, 3, np.nan, 3, 4],
    'The Matrix': [3, 4, np.nan, 4, 3, 5, np.nan, 3, 4, 4],
    'Interstellar': [5, 3, 4, np.nan, 2, 4, 4, 5, 4, 5],
    'Shawshank': [np.nan, 5, 4, 3, 5, 5, 3, 2, np.nan, 3],
}

# Convert to a DataFrame
ratings_df = pd.DataFrame(data, index=['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'])
print("Ratings Matrix:")
print(ratings_df)

#calculate Pearson similarity
def pearson_similarity(user1_ratings, user2_ratings):
#getting common items where both users have ratings
    common_items = user1_ratings.notna() & user2_ratings.notna()
    if not common_items.any():
        return 0  # No common ratings
    
#Calculate Pearson correlation for common items
    return pearsonr(user1_ratings[common_items], user2_ratings[common_items])[0]

#find similar users
def find_similar_users(target_user, ratings_df, num_users=3):
    similarities = {}
    for user in ratings_df.index:
        if user != target_user:
            similarity = pearson_similarity(ratings_df.loc[target_user], ratings_df.loc[user])
            similarities[user] = similarity
    
# Sort by similarity score, highest first
    similar_users = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    return similar_users[:num_users]

#generate recommendations
def recommend_items(target_user, ratings_df, num_recommendations=3):
    similar_users = find_similar_users(target_user, ratings_df)
    target_user_ratings = ratings_df.loc[target_user]
    recommendations = {}
    
    for similar_user, similarity in similar_users:
        similar_user_ratings = ratings_df.loc[similar_user]
        
#look for items not rated by the target user but rated by the similar user
        for item in ratings_df.columns:
            if pd.isna(target_user_ratings[item]) and not pd.isna(similar_user_ratings[item]):
                if item not in recommendations:
                    recommendations[item] = 0
                recommendations[item] += similar_user_ratings[item] * similarity
    
#sort recommendations by the weighted score, highest first
    recommended_items = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [item for item, score in recommended_items[:num_recommendations]]

#generate recommendations for a target user
target_user = 'Charlie'
recommended_items = recommend_items(target_user, ratings_df)
print(f"\nRecommended items for {target_user}: {recommended_items}")
