r_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t',
                      names=r_cols, usecols=range(4), encoding="latin1")

movie_rating = pd.merge(movies, ratings)
lens = pd.merge(movie_rating, users)
