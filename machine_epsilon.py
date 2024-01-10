# TODO

pre_loop_eps = 1*(1/2)   # 1ループ進んだepsである。while文の条件として利用する。
eps = 1                  # マシンイプシロン（eps）の初期値を0にする。

while (1 + pre_loop_eps) > 1: # while文の条件が成立しなくなった時の"eps"の値が、求めたいマシンイプシロンの値である。
    pre_loop_eps *= 1/2   # pre_loop_epsを(1/2)にする。
    eps *= 1/2            # epsの値を(1/2)にする。

print(eps)           # マシンイプシロンを表示する。（結果は、2.220446049250313e-16）
