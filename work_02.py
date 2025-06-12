import random #ランダムモジュール
import time #時間モジュール


t = random.randint(5,15)
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
