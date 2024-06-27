import pandas as pd
from scipy import spatial

# Load the dataset
df = pd.read_csv('ratings.csv')

# Calculate similarity between users using cosine similarity
def calculate_similarity(user1, user2):
    ratings1 = df.loc[user1, :]
    ratings2 = df.loc[user2, :]
    similarity = 1 - spatial.distance.cosine(ratings1, ratings2)
    return similarity

# Find similar users for a given user
def find_similar_users(user, num_similar_users):
    similarities = {}
    for other_user in df.index:
        if other_user != user:
            similarity = calculate_similarity(user, other_user)
            similarities[other_user] = similarity
    similar_users = sorted(similarities, key=similarities.get, reverse=True)[:num_similar_users]
    return similar_users

# Get recommended movies for a given user
def get_recommended_movies(user, similar_users):
    recommended_movies = []
    for similar_user in similar_users:
        movies_rated_by_similar_user = df.loc[similar_user, :].nonzero()[0]
        for movie in movies_rated_by_similar_user:
            if movie not in df.loc[user, :].nonzero()[0]:
                recommended_movies.append(movie)
    return recommended_movies

# Rank recommended movies based on average rating
def rank_recommended_movies(user, recommended_movies):
    average_ratings = {}
    for movie in recommended_movies:
        ratings = []
        for similar_user in find_similar_users(user, 5):
            rating = df.loc[similar_user, movie]
            if rating > 0:
                ratings.append(rating)
        average_rating = sum(ratings) / len(ratings)
        average_ratings[movie] = average_rating
    ranked_movies = sorted(average_ratings, key=average_ratings.get, reverse=True)
    return ranked_movies

# Example usage:
user_id = 1
num_similar_users = 5
recommended_movies = get_recommended_movies(user_id, find_similar_users(user_id, num_similar_users))
ranked_movies = rank_recommended_movies(user_id, recommended_movies)
print("Recommended movies for user", user_id, ":", ranked_movies)
