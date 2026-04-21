import numpy as np

print("行列の作成")
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(type(a))
print(a.shape)

print("\n行の参照")
print(a[0])

print("\n列の参照")
print(a[:,0])

print("\nスライス指定も可能")
print(a[0:2])
print(a[:,0:2])

print("\n「行列 + 1」は全要素に対する和を実行")
print(a + 1)

print("\n *演算子も同様。")
print(a * 2)

print("\n行列演算ではない！")
print(a * a)

print("\n転置行列")
print(a.T)

print("\n内積を求めるにはdot関数を使う")
print(np.dot(a, a.T))

print("\n逆行列")
print(np.linalg.inv(np.dot(a, a.T)))

print("\nゼロ行列、1行列、対角行列")
print(np.zeros((2, 3)))
print(np.ones((2, 3)))
print(np.eye(3))

print("\
特定範囲内で幅を指定してサンプル点を用意。\n\
例えば\n\
定義域「-10〜10の範囲で0.1刻みでサンプル点を用意」みたいなときに便利。\
")
print(np.arange(0, 1, 0.3))

print("\nnp.arangeで始点、刻み幅を省略すると0から指定個数の整数を用意。")
print(np.arange(8))

print("\n行列の形を変形できる")
print(np.reshape(np.arange(6), (2, 3)))

print("\n刻み幅はどうでも良いからサンプル数を指定したい場合に便利。")
print(np.linspace(0, 2, 3))
print(np.linspace(0, 2, 4))

print("\n\
行列を結合できる。\n\
縦方向に結合\
")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
print(np.r_[a, b])

print("横方向に結合")
print(np.c_[a, b])

print()
print("------ 演習問題 ------")
print()
# 演習問題

print("\n1. ベクトル演算の演習\n")

print("\n(1) 5個の要素を持つ列ベクトルを作成せよ。値は全て1とする。")
a = np.ones((5, 1))
print(a)

print("\n(2) 1で作成した列ベクトルのうち、2番目の要素を3.14に更新せよ。なおインデックスは0から数える（0番目、1番目、2番目、、）ものとする。")
a[1, 0] = 3.14
print(a)

print("\n(3) 2で作成した列ベクトルを複製し、転置により行ベクトルに変換せよ。")
b = a.copy().T
print(b)

print("\n(4) 用意した列ベクトルと行ベクトルの内積を求めよ。")
print(np.dot(a, b))

print("\n(5) np.random.randを用いて、10個の要素を持つ列ベクトルを作成せよ。")
c = np.random.rand(10, 1)
print(c)


print("\n2. 行列演算の演習行列演算の演習\n")

print("\n(6) np.random.normalを用いて、平均値10、標準偏差2の正規分布に基づく、2行5列の行列を作成せよ。")
d = np.random.normal(10, 2, (2, 5))
print(d)

print("\n(7) 6で作成した行列から、2列目の要素を抜き出だせ。")
print(d[:, 1])

print("\n(8) 6で作成した行列から、3列目と4列目の要素を抜き出せ。")
print(d[:, 2:4])

print("\n(9) np.random.randで5行2列の行列を用意し、6で用意した行列との積を求めよ。")
e = np.random.rand(5, 2)
print(np.dot(d, e))