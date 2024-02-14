# movie ratings 
ratings = [
    (1, "The Shawshank Redemption", 5),
    (1, "The Godfather", 5),
    (1, "The Dark Knight", 4),
    (1, "Pulp Fiction", 4),
    (1, "Forrest Gump", 3),
    (2, "The Shawshank Redemption", 4),
    (2, "The Godfather", 5),
    (2, "The Dark Knight", 5),
    (2, "Pulp Fiction", 4),
    (2, "Forrest Gump", 3),
    (3, "The Shawshank Redemption", 3),
    (3, "The Godfather", 4),
    (3, "The Dark Knight", 5),
    (3, "Pulp Fiction", 4),
    (3, "Forrest Gump", 2)
]

# movies
movies = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction",
    "Forrest Gump"
]

# Function to recommend movies for a user
def recommend_movies(user_id):
    user_ratings = [rating for rating in ratings if rating[0] == user_id]
    user_ratings.sort(key=lambda x: x[2], reverse=True)
    recommended_movies = [movie for movie in movies if (user_id, movie, 5) not in user_ratings][:5]
    return recommended_movies

# Simple text-based user interface
while True:
    print("\n=== Movie Recommendation System ===")
    user_id = input("Enter your user ID (1, 2, or 3) or 'q' to quit: ")
    if user_id.lower() == 'q':
        break
    try:
        user_id = int(user_id)
        if user_id < 1 or user_id > 3:
            print("Invalid user ID. Please enter 1, 2, or 3.")
            continue
        recommended_movies = recommend_movies(user_id)
        print("\nRecommended movies for user", user_id, ":")
        for i, movie in enumerate(recommended_movies, 1):
            print(i, ".", movie)
    except ValueError:
        print("Invalid input. Please enter a valid user ID or 'q' to quit.")
