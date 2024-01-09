a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO

# 61(aの値)が素数であることの確認
for i in range(2, int(a)):
    if int(a) % i == 0:    # 割り切れると素数ではないことがわかる。
        print(f'{a}(aの値)は素数ではありません')
        break              # break文によって繰り返しを終える。
    if i == (int(a) - 1):  # iが最後の値（a-1）になった場合、aは素数である。
        print(f'{a}(aの値)は素数です')


# 10(bの値)が素数でないことの確認
for j in range(2, int(b)):
    if int(b) % j == 0:    # 割り切れると素数ではないことがわかる。
        print(f'{b}(bの値)は素数ではありません')
        break              # break文によって繰り返しを終える。
    if j == (int(b) - 1):  # jが最後の値（b-1）になった場合、bは素数である。
        print(f'{b}(bの値)は素数です')
