a,b = map(int,input().split())
A = a%4
ans1 = 0
for i in range(A):
    ans1 = ans1^(a-i-1)
B = (b+1)%4
ans2 = 0
for i in range(B):
    ans2 = ans2^(b-i)
print(ans1^ans2)