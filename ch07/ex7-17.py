atleast_100 = movie_stats['rating']['size'] >= 100
movie_stats[atleast_100].sort_values(by=[('rating', 'mean')],
  ascending=False)[:15]
