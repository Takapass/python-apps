import random
import time
import mysql.connector
from datetime import datetime

# ------------------------
# データベース接続
# ------------------------
conn = mysql.connector.connect(
    host="localhost",
    user="",          # ← あなたのMySQLユーザー名に変更
    password="",  # ← あなたのMySQLパスワードに変更
    database="work_02"
)
cursor = conn.cursor(dictionary=True)

# ------------------------
# ユーザー名の入力
# ------------------------
user_name = input("ユーザー名を入力してください: ")

# 前回の記録を取得して表示
cursor.execute("SELECT * FROM work_02_records WHERE name = %s ORDER BY id DESC LIMIT 1;", (user_name,))
last_record = cursor.fetchone()
if last_record:
    print("===== 前回の記録 =====")
    print(f"ユーザー: {last_record['name']}")
    print(f"id: {last_record['id']}")
    print(f"記録時間: {last_record['record_time']} 秒")
    print(f"開始時刻: {last_record['started_at']}")
    print("======================")

# 自分のこれまでのハイスコア
cursor.execute("SELECT MIN(record_time) AS best_time FROM work_02_records WHERE name = %s;", (user_name,))
best_record = cursor.fetchone()
if best_record and best_record["best_time"] is not None:
    print(f"あなたのこれまでの最高記録: {best_record['best_time']} 秒")

# 全体のランキング上位5件
cursor.execute("SELECT name, record_time, started_at FROM work_02_records ORDER BY record_time ASC LIMIT 5;")
top_records = cursor.fetchall()
if top_records:
    print("===== 全体ランキング 上位5件 =====")
    for i, rec in enumerate(top_records, start=1):
        print(f"{i}. {rec['name']} - {rec['record_time']} 秒 ({rec['started_at']})")
    print("===============================")

# ------------------------
# 元の処理
# ------------------------
t = random.randint(5, 15)
print(f"待つ秒数：{t}秒")

time.sleep(t)

start_time = time.time()
print(f"開始時刻:{start_time}")

print("!!!!!")
input("エンターキーを押してください:")

end_time = time.time()
print(f"終了時刻:{end_time}")

lt = end_time - start_time
print(f"かかった時間:{lt}秒")
if lt < 0.01:
    print("不正をしていますね！")

print("エンターキーが押されました")

# ------------------------
# 結果をデータベースに保存
# ------------------------
started_at = datetime.fromtimestamp(start_time)  # 実行開始の時刻
#cursor.execute(
#    "INSERT INTO work_02_records (name, record_time, started_at) VALUES (%s, %s, %s)",
#    (user_name, lt, started_at)
#)
#conn.commit()

#print("結果を保存しました！")

if lt >= 0.01:  # 不正でない場合のみ保存
    cursor.execute(
        "INSERT INTO work_02_records (name, record_time, started_at) VALUES (%s, %s, %s)",
        (user_name, lt, started_at)
    )
    conn.commit()
    print("結果を保存しました！")
else:
    print("結果は保存されませんでした（不正判定）")

# ------------------------
# 終了処理
# ------------------------
cursor.close()
conn.close()
