input()
*W,=map(int,input().split())
print(min(abs(sum(W[:i])-sum(W[i:]))for i in range(1,len(W))))