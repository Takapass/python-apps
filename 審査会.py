import random
# ランダムモジュールを使ってコンピュータがグー、チョキ、パーをランダムに出す
# 勝ち、負け、引き分けの回数を表示するために０を代入した関数を３つ用意する
hands = ["グー", "チョキ", "パー"]
win_count = 0
lose_count = 0
draw_count = 0

while True:
    # ゲームの説明
    print("じゃんけん")
    # 数字を使って出す手を選択
    print("0:グー", "1:チョキ", "2:パー", "9:終了")
    player = int(input("手を選んでください"))
    # 9を入力すれば終われるようにする
    if player == 9:
        print(f"終了!勝ち:{win_count},負け:{lose_count},引き分け:{draw_count}")
        break
    # 0,1,2以外の数字は受け付けないようにする
    if player not in [0, 1, 2]:
        print("無効な入力です")
        continue
    # コンピュータが出す手を０〜２のランダムな数字で取得
    computer = random.randint(0, 2)
    print(f"コンピューター:{hands[computer]}")
    # コンピュータとプレイヤーの勝敗を数字の大小で決めれるようにする
    # 勝ち、負け、引き分けの回数を追加していく
    if player == computer:
        print("あいこ")
        draw_count += 1

    elif (player - computer) % 3 == 1:
        print("あなたの勝ち")
        win_count += 1

    else:
        print("コンピュータの勝ち")
        lose_count += 1