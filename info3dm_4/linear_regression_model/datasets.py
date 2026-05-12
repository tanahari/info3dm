import numpy as np

def load_linear_example1():
    X = np.array([[1, 4], [1, 8], [1, 13], [1, 17]])
    Y = np.array([7, 10, 11, 14])
    return X, Y

# 4週目の講義
def load_nonliner_example1():
    X = np.array([[1, 0.0], [1, 2.0], [1, 3.9], [1, 4.0]])
    Y = np.array([4.0, 0.0, 3.0, 2.0])
    return X, Y

def polynomial2_features(input):
    poly2 = input[:, 1:]**2
    return np.c_[input, poly2]

def polynomial_features(input, degree=3):
    x = input[:, 1]
    features = input  # [1, x]
    for i in range(2, degree + 1):
        features = np.c_[features, x**i]
    return features