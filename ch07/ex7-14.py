movie_rating = pd.merge(movies, ratings)
lens = pd.merge(movie_rating, users)
