N = int(input())
F = 11

for i in range(1,int((N+1)**0.5)+1):
    if N%i==0:
        F=min(F,max(len(str(i)),len(str(int(N/i)))))
print(F)
