Movie Recommendation System

This project demonstrates a simple movie recommendation system using collaborative filtering. The system utilizes a user-item rating matrix and Pearson correlation to calculate user similarities and generate personalized movie recommendations.
Features

Pearson Similarity Calculation: Computes similarity between users based on their common ratings.
Similar User Identification: Identifies the top similar users for a target user.
Personalized Recommendations: Suggests movies to the target user based on ratings by similar users.
Data

The input data is a user-item rating matrix with the following characteristics:
Rows represent users.
Columns represent movies.
Ratings range from 1 to 5 (higher is better), with missing values (NaN) indicating unrated movies.
Example rating matrix:
             The Dark Knight  Inception  The Matrix  Interstellar  Shawshank
Alice                     5        4.0        3.0          5.0        NaN
Bob                       4        NaN        4.0          3.0        5.0
Charlie                   3        4.0        NaN          4.0        4.0
Diana                   NaN        5.0        4.0          NaN        3.0
Eve                       1        2.0        3.0          2.0        5.0
Frank                     5        4.0        5.0          4.0        5.0
Grace                     4        3.0        NaN          4.0        3.0
Hank                      3        NaN        3.0          5.0        2.0
Ivy                       2        3.0        4.0          4.0        NaN
Jack                    NaN        4.0        4.0          5.0        3.0

How It Works

Pearson Correlation:
Identifies common items rated by both users.
Computes the similarity score using the formula:

Returns a similarity score between -1 (completely dissimilar) and 1 (identical).
Find Similar Users:
Compares the target user's ratings with all other users in the matrix.
Ranks users by similarity score (highest to lowest).
Generate Recommendations:
For movies not rated by the target user, predicts a score based on ratings by similar users, weighted by similarity.

Installation
1. Clone the repository:
    git clone <repository-url>
    cd <repository-folder>

2. Install dependencies:
    pip install pandas numpy scipy

3. Run the script:
    python recommendation_system.py

Usage:
Generate Recommendations
1. Update the ratings_df DataFrame with your data.
2. Set the target_user in the script.
3. Run the script to see personalized movie recommendations.

Example Output:
Ratings Matrix:
             The Dark Knight  Inception  The Matrix  Interstellar  Shawshank
Alice                     5        4.0        3.0          5.0        NaN
...

Recommended items for Charlie: ['The Dark Knight', 'The Matrix', 'Shawshank']

Future Enhancements:
1. Support for more advanced similarity measures (e.g., cosine similarity).
2. Handle large datasets using sparse matrix representations.
3. Implement a graphical interface for user interaction.


License:
This project is licensed under the MIT License. See the LICENSE file for details.

