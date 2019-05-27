import numpy as np

def pearson_coefficient(u, v):
    u_diff = u - np.mean(u)
    v_diff = v - np.mean(v)
    numerator = np.dot(u_diff, v_diff)
    denominator = np.sqrt(sum(u_diff ** 2)) * np.sqrt(sum(v_diff ** 2))
    return numerator / denominator
