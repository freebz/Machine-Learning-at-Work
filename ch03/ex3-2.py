from math import sqrt

sum = 0

for predict, actual in zip(predicts, actuals):
    sum += (predict - actual) ** 2

sqrt(sum / len(predicts))
