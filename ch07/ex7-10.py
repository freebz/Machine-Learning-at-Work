def adjusted_cosine_coefficient(m, n, u_mean):
    adjusted_m = m - u_mean
    adjusted_n = n - u_mean
    numerator = np.dot(adjusted_m, adjusted_n)
    denominator = np.sqrt(sum(adjusted_m ** 2)) * np.sqrt(sum(adjusted_n ** 2))
    return numerator /denominator
