#!/usr/bin/env python3
# 整数の入力
n = int(input())

def f(a, b):
    #print("a: {}, b:{}".format(a, b))
    digit_a = 0
    while(a > 0):
        digit_a += 1
        a //= 10
    #print("digit_a:{}".format(digit_a))
    digit_b = 0
    while(b > 0):
        digit_b += 1
        b //= 10
    #print("digit_b:{}".format(digit_b))
    if digit_a < digit_b:
        return digit_b
    else:
        return digit_a

#約数列挙
def resolve(n):
    min = 10 ** 10
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            if i != n//i:
                b = n//i
            else:
                b = i
            temp = f(i, b)
            if min > temp:
                min = temp

    print(min)

#print("n: {}".format(n))
resolve(n)