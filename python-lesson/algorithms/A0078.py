import math

S, P = map(int, input().split())

D = S * S - 4 * P

if D < 0:
    print(-1)
else:
    # Kvadrat ildiz butun son bo'lishini aniq tekshiramiz
    sqrtD = int(math.sqrt(D))
    if sqrtD * sqrtD != D:  
        print(-1)
    else:
        x1 = (S + sqrtD) // 2
        x2 = (S - sqrtD) // 2
        print(x1, x2)
        
        # Qo'shimcha tekshiruv: x1 va x2 butun musbat son bo'lishi kerak
        # if x1 + x2 == S and x1 * x2 == P and x1 >= 1 and x2 >= 1:
        #     print(max(x1, x2), min(x1, x2))
        # else:
        #     print(-1)
    