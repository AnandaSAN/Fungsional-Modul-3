from functools import reduce

movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021, "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020, "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

def display_movie_info(title):
    movie = list(filter(lambda x: x['title'] == title, movies))
    if not movie:
        print(f"Film dengan judul {title} tidak ditemukan.")
    else:
        movie = movie[0]
        print(f"Informasi Film: {movie['title']}")
        print(f"Rating: {movie['rating']}")
        print(f"Tahun Rilis: {movie['year']}")
        print(f"Genre: {movie['genre']}")

def count_movies_by_genre():
    genre_count = reduce(lambda x, movie: {**x, movie['genre']: x.get(movie['genre'], 0) + 1}, movies, {})
    return genre_count

def average_rating_by_year():
    year_ratings = reduce(lambda x, movie: {**x, movie['year']: x.get(movie['year'], []) + [movie['rating']],}, movies, {})
    average_ratings = {year: sum(ratings) / len(ratings) for year, ratings in year_ratings.items()}
    return average_ratings

def movie_with_highest_rating():
    highest_rated_movie = max(movies, key=lambda x: x["rating"])
    return highest_rated_movie

def get_movie_titles(movies):
    titles = map(lambda x: x["title"], movies)
    return list(titles)

while True:
    print("\nPilih tugas yang ingin dilakukan:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Menampilkan judul-judul film")
    print("6. Selesai")
    
    choice = input("Masukkan nomor tugas (1/2/3/4/5/6): ")
    
    if choice == '1':
        genre_count = count_movies_by_genre()
        print("Jumlah Film Berdasarkan Genre:")
        print(genre_count)
    elif choice == '2':
        average_ratings = average_rating_by_year()
        print("Rata-rata Rating Film Berdasarkan Tahun Rilis:")
        print(average_ratings)
    elif choice == '3':
        highest_rated_movie = movie_with_highest_rating()
        print("Film dengan Rating Tertinggi:")
        display_movie_info(highest_rated_movie["title"])
    elif choice == '4':
        title = input("Masukkan judul film yang ingin dicari: ")
        display_movie_info(title)
    elif choice == '5':
        movie_titles = get_movie_titles(movies)
        print("Judul-judul Film:")
        print(movie_titles)
    elif choice == '6':
        break
