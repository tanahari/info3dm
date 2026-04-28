import datasets
import regression

print("datasets.py の確認")
X, Y = datasets.load_linear_example1()
print(X)
print(X[0])
print(Y)

print()

print("regression.py ver.1 の確認")
model = regression.LinearRegression()
model.fit(X, Y)
print(model.theta)

print()

print("regression.py ver.2 の確認")
print(model.predict(X))

print()

print("regression.py ver.3 の確認")
print(model.score(X, Y))