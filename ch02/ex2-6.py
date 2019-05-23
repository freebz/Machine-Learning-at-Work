def cross_entropy_error(y, t, eps=1e-15):
    y_clipped = np.clip(y, esp, 1 - esp)
    return -1 * (sum(t * np.log(y_clipped) +
                  (1 - t) * np.log(1 - y_clipped)))
