import random
n = random.randint(1,100)
q = input("1~100までの数字を当ててください")
b = 4
c = 0

while True:
    for i in range(5):
        cnt = cnt + 1
        a = input()
        if n == int(a):
            print(f"正解です{c}回でクリア")
            result = True
            break
        else:
            print(f"不正解です:あと{b}回挑戦出来ます")
            if n < a:
                if n - a > 10:
                    print("今の数より10以上小さいです")
                else:
                    print("もっと小さい数ですが、かなり近いです")
            else:
                if a - n > 10:
                    print("今の数より10以上大きいです")
                else:
                    print("もっと大きい数ですが、かなり近いです")
        
    if result:
        print("クリアです")
    else:
        print(f"残念残念正解は{n}でした")
    
    a = input()
    if a == "No":
        break
    else:
        pass




