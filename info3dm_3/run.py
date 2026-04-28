import datasets
import regression

print("datasets.py の確認")
X, Y = datasets.load_linear_example1()
print(X)
print(X[0])
print(Y)

print()

print("regression.py の確認")
model = regression.LinearRegression()
model.fit(X, Y)
print(model.theta)