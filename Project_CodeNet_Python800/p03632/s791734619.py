import sys
input = sys.stdin.readline

A,B,C,D = list(map(int,input().split()))

push =[0]*102
push[A+1]+=1
push[B+1] -=1
push[C+1] +=1
push[D+1] -= 1
count = 0
for i in range(1,len(push)):
    push[i] = push[i] + push[i-1]
    if push[i]==2:
        count +=1
print(count)
