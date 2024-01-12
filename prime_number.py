a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

# TODO

def is_prime_num(n: int) -> bool:
    """素数のときTrue, 素数でない時Falseを返す。"""
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3.14:                              # 1, 2行目でint型を指定しているため、ここは呼ばれないが、エクストラ問題の解答として記載。
        raise ValueError("整数を入力して下さい")
    if n == -1:
        raise ValueError("正の数を入力して下さい")
    for i in range(2, n):
        if n % i == 0:                         # 割り切れると素数ではないことがわかる。
            return False
        if i == (n - 1):                       # iが最後の値（n-1）になった場合、aは素数である。
            return True

is_prime_num_a = is_prime_num(a)               # 61の素数判定
is_prime_num_b = is_prime_num(b)               # 10の素数判定

print(is_prime_num_a)                          # 結果はTrue
print(is_prime_num_b)                          # 結果はFalse
