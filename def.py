#-*- coding: utf-8 -*
def jdz(x):
    if x >= 0:
        return x
    else:
        return -x

n = float(input('input a number:'))
print(jdz(n))