import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a,b = map(int, input().split())
def sub(a):
    # 0^1^...^a-1
    ans = 0
    for i in range(a.bit_length()):
        l = pow(2,i)
        num = (a//(l*2)) * l + min(l, a%(l*2))
        num1 = a - num
        if num1%2:
            ans += l
    return ans
def sub2(a):
    ans = 0
    for i in range(a):
        ans ^= i
    return ans
ans = sub(b+1) ^ sub(a)
print(ans)