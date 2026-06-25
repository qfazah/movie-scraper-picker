import os
import random
from bs4 import BeautifulSoup
import requests

file_path = "movie_names_file.txt"

# --- STEP 1: SCRAPE AND SAVE MOVIES (Only if the file doesn't exist yet) ---
if not os.path.exists(file_path):
    url = "https://www.empireonline.com/movies/features/best-movies-2/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    all_movies = soup.find_all("h2")

    # Skip the first 3 non-movie headings and save them
    clean_movie_list = all_movies[3:]

    with open(file_path, mode="w", encoding="utf-8") as file:
        for movie in clean_movie_list:
            file.write(movie.get_text() + "\n")
    print("--- Movie list successfully scraped and saved to file! ---\n")

# --- STEP 2: READ, PICK RANDOM, REMOVE, AND UPDATE THE FILE ---
# 1. Open the file in read mode to look at the list
with open(file_path, "r", encoding="utf-8") as file:
    movies = file.readlines()

# Clean up any hidden whitespace or empty lines
clean_movies = [m for m in movies if m.strip()]

# 2. Check if there are any movies left
if not clean_movies:
    print("you saw all movies")
else:
    # 3. Pick a random movie
    random_movie = random.choice(clean_movies)
    print(f"yours today movie : \n {random_movie.strip()}")

    # 4. Remove that chosen movie from our list
    clean_movies.remove(random_movie)

    # 5. Overwrite the file with mode="w" to save the remaining movies
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(clean_movies)