a, b = map(int, input().split())

# n までに2**(i-1)が何個含まれるか

def solve(n, i):
    res = 0
    mod = 2**i
    c = n // mod
    res += c*mod//2
    if n % mod >= mod//2:
        res += (n%mod - mod//2 + 1)
    return res

b_list = [0]*40
a_list = [0]*40
ans = 0
for i in range(1, 41):
    num_l = solve(b, i)
    num_r = solve(a-1, i)
    num_one = num_l - num_r
    if num_one% 2 == 1:
        ans += 2**(i-1)
print(ans)

