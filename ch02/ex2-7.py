def euclidean_distance(a, b):
    return np.sqrt(sum(x - y) ** 2 for (x, y) in zip(a, b))
