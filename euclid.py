import random                          # randomモジュールをimport
import math

a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO

# ----- 問3 -----
def cal_gcm(a: int, b: int) -> int:    # 最大公約数(greatest common measure)を求める。
    if a > b:                          # aがbよりも大きい時、aとbを入れ替える。
        a, b = b, a
    while b != 0:
        a, b = b, a % b
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
