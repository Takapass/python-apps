import random

hands = ["グー", "チョキ", "パー"]
win_count = 0
lose_count = 0
draw_count = 0

while True:
    print("じゃんけん")
    print("0:グー","1:チョキ","2:パー","9:終了")
    player = int(input("手を選んでください"))

    if player == 9:
        print(f"終了!勝ち:{win_count},負け:{lose_count},引き分け:{draw_count}")
        break

    if player not in [0,1,2]:
        print("無効な入力です")
        continue

    computer = random.randint(0,2)
    print(f"コンピューター:{hands[computer]}")

    if player == computer:
        print("あいこ")
        draw_count += 1
    
    elif (player - computer) % 3 == 1:
        print("あなたの勝ち")
        win_count += 1

    else:
        print("コンピュータの勝ち")
        lose_count += 1