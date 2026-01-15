import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",          # あなたのMySQLユーザー名
        password="your_pass", # あなたのMySQLパスワード
        database="python_app"    # 使いたいデータベース名
    )
    cursor = conn.cursor()

    cursor.execute("SELECT DATABASE();")
    print("✅ 接続成功！ データベース:", cursor.fetchone())

except mysql.connector.Error as e:
    print("❌ 接続エラー:", e)

finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
