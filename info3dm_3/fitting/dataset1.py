import numpy as np
import unittest
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# 画像保存用のディレクトリを作成
current_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(current_dir, 'results')
os.makedirs(save_dir, exist_ok=True)

# y = sin(pi * x * 0.8) * 10 の実装
def true_function(x):
    y = np.sin(np.pi * x * 0.8) * 10
    return y

# テスト用クラス
class TestTrueFunction(unittest.TestCase):
    def test_x_zero_return_zero(self):
        x = 0
        correct = 0

        y = true_function(x)

        self.assertAlmostEqual(y, correct, places=7)

if __name__=='__main__':
    # --- exercises1.1 ---
    print("exercises1.1")

    # ユニットテスト
    unittest.main(argv=[''], exit=False)

    # 描画
    x = np.linspace(-1, 1, 100)
    y = true_function(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=r'Target Function ($y = 10\sin(0.8\pi x)$)', color='blue')
    plt.title('演習1.1：真の関数の準備')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    save_path = os.path.join(save_dir, 'ex1.1.png')
    plt.savefig(save_path)

    print()

    # --- exercises1.2 ---

    print("exercises1.2")

    np.random.seed(0)
    n = 20
    x_sample = np.random.uniform(-1, 1, n)
    y_sample = true_function(x_sample)

    df = pd.DataFrame({
        '観測点': x_sample,
        '真値': y_sample
    })

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=r'Target Function ($y = 10\sin(0.8\pi x)$)', color='blue')
    plt.scatter(df['観測点'], df['真値'], color='red', s=40, edgecolors='black', label='サンプル集合 (n=20)', zorder=3)
    plt.title('演習1.2：観測点と真値の準備')
    plt.xlabel('観測点 (x)')
    plt.ylabel('真値 (y)')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    save_path = os.path.join(save_dir, 'ex1.2.png')
    plt.savefig(save_path)


    print()

    # --- exercises1.3 ---

    print("exercises1.3")

    noise_raw = np.random.normal(loc=0.0, scale=np.sqrt(2.0), size=20)
    noise_half = noise_raw * 0.5
    df['観測値'] = df['真値'] + noise_half

    plt.figure(figsize=(8, 5))
    x_line = np.linspace(-1, 1, 100)
    plt.plot(x, y, label=r'Target Function ($y = 10\sin(0.8\pi x)$)', color='blue')
    plt.scatter(df['観測点'], df['真値'], color='red', s=40, edgecolors='black', label='サンプル集合 (n=20)', zorder=3)
    plt.scatter(df['観測点'], df['観測値'], color='green', marker='x', s=40, label='観測値 (Noisy Data)')
    plt.title('ノイズを付与した観測値の準備')
    plt.xlabel('観測点 (x)')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    save_path = os.path.join(save_dir, 'ex1.3.png')
    plt.savefig(save_path)