def ratings_summary(title_list, ratings_list):
    total_movies = len(title_list)
    average_rating = sum(ratings_list) / total_movies

    return  total_movies, average_rating


movie_program = False
movie_titles, movie_ratings = [], []
start = input("Start Movie Rating Tracker? (y/n): ")

if start == "y":
    movie_program = True
    print("Welcome to Movie Rating Tracker")
elif start == "n":
    print("Closing program")
else:
    print("Please enter y or n")

while movie_program:
    movie_title = ""
    movie_rating = "-1"

    while movie_title == "":
        movie_title = input("Enter Movie Title: ")
    else:
        movie_titles.append(movie_title)

    while not (0<= float(movie_rating) <= 10):
        movie_rating  = input("Enter Movie Rating (0-10): ")
    else:
        movie_ratings.append(float(movie_rating))

    new_entry = input("Add another movie? (y/n): ")

    if new_entry == "y":
        continue
    else:
        print("Closing program")
        movie_program = False

if movie_ratings and movie_titles:
    print("\nMovie Ratings Summary:")
    summary = ratings_summary(movie_titles, movie_ratings)
    print(f"You have rated {summary[0]} movies with an average rating of {round(summary[1], 2)}")