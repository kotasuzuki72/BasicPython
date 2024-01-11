a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

remainder = 1 # 最初は、余り（remainder）を0ではない値に設定する。

if int(a) > int(b):  # aがbよりも大きい時、aとbを入れ替える。
    a, b = b, a

while not remainder == 0:          # 余りが0になるまで繰り返す。
    quotient = int(b) // int(a)    # 商(quotient)を求める。
    remainder = int(b) % int(a)    # 余りを求める。
    if remainder == 0:             # 余りが0になった場合、whileループを抜ける。
        break
    else:                          # 余りが0でない場合は、次のループのためにaとbの値を更新する。
        b = a
        a = remainder

print(f'最大公約数は {a} です。')
