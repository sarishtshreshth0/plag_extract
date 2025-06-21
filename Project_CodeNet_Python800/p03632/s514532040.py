A,B,C,D = list(map(int,input().split()))
N = sum([1 for i in range(0,101) if A < i <= B and C < i <=D])
print(N)