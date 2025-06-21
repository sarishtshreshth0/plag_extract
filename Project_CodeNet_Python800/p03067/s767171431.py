A,B,C=map(int,input().split())
A,B=min(A,B),max(A,B)
print("Yes" if A<=C<=B else "No")