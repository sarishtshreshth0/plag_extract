N = int(input())
a=0
n=N
while n!=0:
    a+=n%10
    n//=10
print("Yes"if N%a==0 else "No")