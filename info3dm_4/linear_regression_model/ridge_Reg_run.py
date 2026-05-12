import regression
import datasets
import numpy as np
import matplotlib.pyplot as plt

DEGREE = 3

X, Y = datasets.load_nonliner_example1()
ex_X = datasets.polynomial_features(X, degree=DEGREE)

X_plot = np.linspace(-1.5, 5.5, 200)
X_plot = np.c_[np.ones(len(X_plot)), X_plot]
ex_X_plot = datasets.polynomial_features(X_plot, degree=DEGREE)

#alphas = [0.0, 0.1, 0.5, 1.0, 10.0, 100]
alphas = np.arange(0, 3, 0.0001)
plt.figure(figsize=(10, 6))
plt.scatter(X[:, 1], Y, color='black', label='Original Data', zorder=5)

print(f"degree={DEGREE}")
for alpha in alphas:
    model = regression.RidgeRegression(alpha)
    model.fit(ex_X, Y)

    y_pred = model.predict(ex_X_plot)

    plt.plot(X_plot[:, 1], y_pred, label=f'alpha={alpha}')

    #print(f"alpha={alpha:4}: theta={model.theta}")

# --- グラフの表示範囲を指定 ---
plt.xlim(-2.0, 6.5)  # X軸を-1から5までに設定
plt.ylim(-6, 8)  # Y軸を-6から8までに設定

# --- 軸のラベルやタイトル ---
plt.title(f"Ridge Regression with different alphas (degree={DEGREE})")
plt.xlabel("X")
plt.ylabel("Y")
#plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()