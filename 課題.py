import random

hands = ["グー", "チョキ", "パー"]
#勝ち負けのカウント
win_count = 0   
lose_count = 0  
draw_count = 0 

#ループさせる
while True:
    print("\n--- じゃんけん ---")
    #数字と手を対応
    print("0: グー, 1: チョキ, 2: パー, 9: 終了")
    player = int(input("あなたの手は？: "))

    if player == 9:
        print(f"終了！勝ち: {win_count}, 負け: {lose_count},引き分け:{draw_count}")
        break

    #0,1,2以外は無効
    if player not in [0, 1, 2]:
        print("無効な入力です。")
        continue

    #コンピュータの手を決める
    computer = random.randint(0, 2)
    print(f"コンピュータ: {hands[computer]}")

    if player == computer:
        print("あいこ！")
        draw_count += 1
    elif (player - computer) % 3 == 1:
        print("あなたの勝ち！")
        win_count += 1
    else:
        print("あなたの負け！")
        lose_count += 1
