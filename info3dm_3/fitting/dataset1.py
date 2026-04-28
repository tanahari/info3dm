import numpy as np
import unittest
import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
font_path = '/Library/Fonts/Arial Unicode.ttf'
font_prop = font_manager.FontProperties(fname = font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# 画像保存用のディレクトリを作成
current_dir = os.path.dirname(os.path.abspath(__file__))
save_dir = os.path.join(current_dir, 'results')

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
    # ユニットテスト
    unittest.main(argv=[''], exit=False)

    # 描画
    x = np.linspace(-1, 1, 100)
    y = true_function(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=r'Target Function ($y = 10\sin(0.8\pi * x)$)', color='blue')
    plt.title('データマイニング：事象の可視化')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    save_path = os.path.join(save_dir, 'ex1.1.png')
    plt.savefig(save_path)