N = int(input())

out=10**10
for A in range(1,int(N**(1/2))+2):
    if N%A == 0:
        B = N//A
        KA, KB = len(str(A)), len(str(B))
        dam = max(KA,KB)
        out=min(out,dam)

print(out)