s=input()
S=[s[i] for i in range(len(s))]
A=['0','1']
B=[A[i%2] for i in range(len(S))]
count=0
for i in range(len(S)):
  if S[i]!=B[i]:
    count=count+1
print(min(count,len(S)-count))