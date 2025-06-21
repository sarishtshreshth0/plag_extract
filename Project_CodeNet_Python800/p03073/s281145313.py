S=input()
d0=0
d1=0
for i in range(len(S)):
    d0+=int(S[i])!=i%2
    d1+=int(S[i])!=(i+1)%2
print(min(d0,d1))