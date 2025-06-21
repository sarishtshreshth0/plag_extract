Q, H, S, D = map(int, input().split())
N = int(input())
x = N % 2
y = N // 2
arr = [4*Q*x, 2*H*x, S*x]
arr1 = [8*Q*y, 4*H*y, 2*S*y, D*y]
#if N % 2 == 0:
#  arr.append(int(0.5*D*N))
#else:
#  arr.append(int(0.5*D*(N-1)+ min(S, 2*H, 4*Q)))
   
print(min(arr) + min(arr1))