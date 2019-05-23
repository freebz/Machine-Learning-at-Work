import numpy as np

# 퍼셉트론을 이용한 예측
def predict(w, x):
    sum = np.dot(w, x)

    if sum >= 0:
        return 1
    else:
        return -1
