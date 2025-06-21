n=int(input())
s=input()
cnt=0
for i in s:
    if i=="(": cnt+=1
    elif cnt>=1: cnt-=1
cnt2=0
for i in range(n-1,-1,-1):
    if s[i]==")": cnt2+=1
    elif cnt2>=1: cnt2-=1
print("("*cnt2+s+")"*cnt)