from math import sin
import math                                    # 円周率を使うためのimport
# --example--
# print(sin(0))
# >>> 0
# -----------

def cal_integral(f, a=0, b=1, n=100) -> float: # 実装した関数
    S = 0                                      # 積分値
    h = (b-a)/n                                # 1つの区間の幅

    for i in range(n):                         # n(分割数)回、計算を繰り返す。
        S += (h/2) * (f(a+i*h)+f(a+(i+1)*h))   # iは0から(N-1)であるため、台形公式において(k-1)=iとする。
    
    return S

def q2_function(x: float) -> float:            # (2)で用いる関数
    return 4/(1+x*x)

def q3_function(x: float) -> float:            # (3)で用いる関数
    return ((math.pi)**(1/2)) * (math.exp(-x**2))


q1 = cal_integral(sin, 0, (1/2)*(math.pi), 50)
q2 = cal_integral(q2_function, 0, 1, 100)
q3 = cal_integral(q3_function, -100, 100, 1000)

print(q1)                                      # 結果は0.9999177519437218
print(q2)                                      # 結果は3.141575986923131
print(q3)                                      # 結果は3.1415926535897944
