N = int(input())
ans = N//500 * 1000
N = N%500
ans += N//5 * 5
print(ans)