def load_data(filename, path="ml-100k/"):
    data = []
    y = []
    with open(path + filename) as f:
        for line in f:
            (user, movieid, rating, ts) = line.split('\t')
            data.append({"user_id": str(user), "movie_id": str(movieid)})
            y.append(float(rating))

    return (data, np.array(y))

(dev_data, y_dev) = load_data("ua.base")
(test_data, y_test) = load_data("ua.test")
