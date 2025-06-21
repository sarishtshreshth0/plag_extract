A,B=map(int,input().split())
ans=0
while True:
    ans=ans^A
    #print(ans)
    if A%4==3:
        break
    A=A+1
#print("\n")
while True:
    ans=ans^B
    #print(ans)
    if B%4==0:
        break
    B=B-1
print(ans)