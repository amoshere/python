#-*- coding: utf-8 -*
## 输入一元二次方程的系数，返回两个解
import math
def quadratic(a,b,c):
    deta = b*b-4*a*c
    if deta > 0:
        x1 = (-b + math.sqrt(deta))/(2*a)
        x2 = (-b - math.sqrt(deta))/(2*a)
        return ('solutions are:%s,%s' % (x1,x2))
    elif deta == 0:
        x1 = -b/(2*c)
        x2 = x1
        return ('solutions are:%s,%s:' % (x1,x2))
    else:
        print("no realistic solution")

