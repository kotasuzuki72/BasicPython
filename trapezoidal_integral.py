from math import sin
import math    # 円周率を使うためのimport
# --example--
# print(sin(0))
# >>> 0
# -----------

S = 0               # 積分値
N = 100             # 分割数
a = 0               # 区間の右端
b = (1/2)*(math.pi) # 区間の左端

h = (b-a)/N         # 1つの区間の幅

for i in range(N):  # N(100)回、計算を繰り返す。
    S += (h/2) * (sin(a+i*h)+sin(a+(i+1)*h)) # iは0から(N-1)であるため、台形公式において(k-1)=iとする。

print(f'sin関数の[{a},{b}]における積分値は、{S}です。') # Sの値は、0.9999794382396072となった。
