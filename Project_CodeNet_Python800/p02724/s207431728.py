N = int(input())
a500 = N //500
N = N - 500 *a500
a5 = N//5
res = 1000*a500 +5*a5
print(res)