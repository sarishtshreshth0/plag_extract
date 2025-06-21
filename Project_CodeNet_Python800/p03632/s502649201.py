A,B,C,D=map(int,input().split())
start=max(A,C)
end=min(B,D)
print(max(0,end-start))
