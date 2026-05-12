import datasets
import regression
import matplotlib.pyplot as plt
import numpy as np

print("datasets.py の確認")
X, Y = datasets.load_nonliner_example1()
ex_X = datasets.polynomial2_features(X)
model = regression.LinearRegression()
model.fit(ex_X, Y)

print(ex_X)
print(Y)

samples = np.arange(0, 4.5, 0.1)
X_samples = np.c_[np.ones(len(samples)), samples]
ex_X_samples = datasets.polynomial2_features(X_samples)

plt.scatter(X[:,1], Y)
plt.plot(samples, model.predict(ex_X_samples))
plt.show()