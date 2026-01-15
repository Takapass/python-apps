import random
import mysql.connector

# --- MySQL接続 ---
conn = mysql.connector.connect(
    host="localhost",
    user="",           # MySQLユーザー名に変更
    password=""  # MySQLパスワードに変更
)
cursor = conn.cursor()

# --- データベース・テーブル作成 ---
cursor.execute("CREATE DATABASE IF NOT EXISTS work_01")
cursor.execute("USE work_01")
cursor.execute("""
CREATE TABLE IF NOT EXISTS number_guess (
    id INT AUTO_INCREMENT PRIMARY KEY,
    answer_number INT NOT NULL,
    attempts INT NOT NULL,
    result VARCHAR(10) NOT NULL,
    play_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

# --- 結果保存関数 ---
def save_result(answer, attempts, result):
    sql = "INSERT INTO number_guess (answer_number, attempts, result) VALUES (%s, %s, %s)"
    cursor.execute(sql, (answer, attempts, result))
    conn.commit()

# --- ゲームループ ---
while True:
    n = random.randint(1, 100)
    b = 4       # 残り挑戦回数
    c = 0       # 試行回数
    result = False  # 結果フラグ

    print("1~100までの数字を当ててください!")

    while b > 0:
        c += 1
        try:
            a = int(input(f"数字を入力 (残り {b} 回): "))
        except ValueError:
            print("数字を入力してください")
            continue

        if a == n:
            print(f"正解です！{c}回でクリア")
            result = True
            break
        else:
            b -= 1
            print(f"不正解です: 残り {b} 回")

            # ヒントの表示
            if a < n:
                diff = n - a
                if diff > 10:
                    print("もっと大きい数です")
                else:
                    print("もう少し大きい数ですが、かなり近いです")
            else:
                diff = a - n
                if diff > 10:
                    print("もっと小さい数です")
                else:
                    print("もう少し小さい数ですが、かなり近いです")

    # 結果を保存
    if result:
        print("クリアです")
        save_result(n, c, 'win')
    else:
        print(f"残念！正解は {n} でした")
        save_result(n, c, 'lose')

    # 再プレイ確認
    again = input("もう一度プレイしますか？(Yes/No): ")
    if again.lower() == "no":
        break

# --- 接続を閉じる ---
cursor.close()
conn.close()
print("ゲーム終了。結果はデータベースに保存されています。")
