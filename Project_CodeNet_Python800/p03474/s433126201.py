A,B=map(int,input().split())
n=str(input())
numbers=['1','2','3','4','5','6','7','8','9','0']
if n[A]!='-':
    print('No')
    exit()
for i in range(A):
    if not(n[i] in numbers):
        print('No')
        exit()
for j in range(B):
    if not(n[j+A+1] in numbers):
        print('No')
        exit()

print('Yes')