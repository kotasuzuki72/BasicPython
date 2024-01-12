import random                          # randomモジュールをimport
import math

a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO

# ----- 問3 -----
def cal_gcm(a: int, b: int) -> int:    # 最大公約数(greatest common measure)を求める。
    remainder = 1                      # 最初は、余り（remainder）を0ではない値に設定する。

    if a > b:                          # aがbよりも大きい時、aとbを入れ替える。
        a, b = b, a
    
    while not remainder == 0:          # 余りが0になるまで繰り返す。
        quotient = int(b) // int(a)    # 商(quotient)を求める。
        remainder = int(b) % int(a)    # 余りを求める。
        if remainder == 0:             # 余りが0になった場合、whileループを抜ける。
            break
        else:                          # 余りが0でない場合は、次のループのためにaとbの値を更新する。
            b = a
            a = remainder
    
    return a

gcm = cal_gcm(a, b)
print(f'最大公約数は {gcm} です。')

# ----- 問4 -----

def is_coprime(a: int, b: int) -> bool: # 互いに素である(coprime)か判定。返り値がboolより、is~と命名
    gcm = cal_gcm(a, b)                 # 問3の関数を使用。
    if gcm == 1:
        return True
    else:
        return False

is_coprime_a_b = is_coprime(a, b)
print(is_coprime_a_b)

# ----- 問4 エクストラ問題 -----

coprime_c_d_count = 0                   # 最初は、互いに素である回数を0にする。
for_roop_num_count = 0                  # 最初は、forループが回った回数を0にする。

for i in range(100000):
    c = random.randint(1, 10000)        # 1万以下の2つの自然数をランダムに生成。
    d = random.randint(1, 10000)        # 変数a,bはすでに使用しているため、代わりに変数c,dを使用。
    is_coprime_c_d = is_coprime(c, d) 
    if is_coprime_c_d:                  # 互いに素である回数をカウント
        coprime_c_d_count += 1        
    for_roop_num_count += 1
    
print(f'エクストラ問題の確率は、{coprime_c_d_count/for_roop_num_count}です') # 結果は、0.60772（実行するごとに変化する）
print(f'6/(π*π)の値は、{6/((math.pi)**2)}です')                            # 結果は、0.6079271018540267
