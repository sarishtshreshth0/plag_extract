from collections import Counter
N=int(input())
A=[int(x) for x in input().split()]
B=[0]*N
left=0
for i in range(N):
  left+=A[i]
  B[i]=left
count=Counter(B)
score=0
for num,freq in zip(count,count.values()):
  if num==0:
    score+=freq*(freq-1)/2+freq
  else:
    score+=freq*(freq-1)/2
print(int(score))