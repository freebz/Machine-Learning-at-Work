import numpy as np
def perceptron_hinge_loss(w, x, t):
    loss = 0
    for (input, label) in zip(x, t):
        v = label * np.dot(w, input)
        loss += max(0, -v)
    return loss
