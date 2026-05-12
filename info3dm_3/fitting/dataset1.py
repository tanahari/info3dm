import numpy as np
import unittest
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

# --- 設定（グローバル） ---
font_path = '/Library/Fonts/Arial Unicode.ttf'
if os.path.exists(font_path):
    font_prop = font_manager.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()

# ディレクトリ設定
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_DIR = os.path.join(CURRENT_DIR, 'results')
os.makedirs(SAVE_DIR, exist_ok=True)
TSV_PATH = os.path.join(SAVE_DIR, 'dataset.tsv')

# --- 共通関数 ---
def true_function(x):
    """y = 10 * sin(0.8 * pi * x)"""
    return np.sin(np.pi * x * 0.8) * 10

# --- テスト用クラス ---
class TestTrueFunction(unittest.TestCase):
    def test_x_zero_return_zero(self):
        self.assertAlmostEqual(true_function(0), 0, places=7)

# --- 各演習の関数定義 ---

def exercise1_1():
    print("--- exercises1.1 ---")
    # ユニットテストの実行
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTrueFunction)
    unittest.TextTestRunner(verbosity=1).run(suite)

    # 描画
    x = np.linspace(-1, 1, 100)
    y = true_function(x)

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=r'$y = 10\sin(0.8\pi x)$', color='blue')
    plt.title('演習1.1：真の関数の準備')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.savefig(os.path.join(SAVE_DIR, 'ex1.1.png'))
    plt.close() # メモリ解放のために閉じる

def exercise1_2():
    print("--- exercises1.2 ---")
    np.random.seed(0)
    n = 20
    x_sample = np.random.uniform(-1, 1, n)
    y_sample = true_function(x_sample)

    df = pd.DataFrame({'観測点': x_sample, '真値': y_sample})

    # 描画
    x_line = np.linspace(-1, 1, 100)
    plt.figure(figsize=(8, 5))
    plt.plot(x_line, true_function(x_line), color='blue', alpha=0.5)
    plt.scatter(df['観測点'], df['真値'], color='red', label='サンプル(n=20)')
    plt.title('演習1.2：観測点と真値')
    plt.legend()
    plt.savefig(os.path.join(SAVE_DIR, 'ex1.2.png'))
    plt.close()
    
    return df

def exercise1_3(df):
    print("--- exercises1.3 ---")
    noise = np.random.normal(loc=0.0, scale=np.sqrt(2.0), size=len(df)) * 0.5
    df['観測値'] = df['真値'] + noise

    # 描画
    plt.figure(figsize=(8, 5))
    plt.scatter(df['観測点'], df['真値'], color='red', label='真値')
    plt.scatter(df['観測点'], df['観測値'], color='green', marker='x', label='観測値(Noisy)')
    plt.title('演習1.3：ノイズ付与')
    plt.legend()
    plt.savefig(os.path.join(SAVE_DIR, 'ex1.3.png'))
    plt.close()
    
    return df

def exercise1_4(df):
    print("--- exercises1.4 ---")
    df.to_csv(TSV_PATH, sep='\t', index=False, encoding='utf-8')
    print(f"保存完了: {TSV_PATH}")

def exercise1_5():
    print("--- exercises1.5 ---")
    if not os.path.exists(TSV_PATH):
        print("エラー: ファイルが存在しません。先に1.4を実行してください。")
        return None
    
    df_loaded = pd.read_csv(TSV_PATH, sep='\t', encoding='utf-8')
    print("読み込みデータ確認:")
    print(df_loaded.head())
    return df_loaded

# このファイル自体を直接実行した時の動作
if __name__ == '__main__':
    exercise1_1()
    df_sample = exercise1_2()
    df_noisy = exercise1_3(df_sample)
    exercise1_4(df_noisy)
    df_final = exercise1_5()