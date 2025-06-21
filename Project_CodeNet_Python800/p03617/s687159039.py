Q,H,S,D = map(int,input().rstrip().split(' '))
N = int(input())
 
one = min(S,2*H,4*Q)
two = min(D,2*one)
 
ans = two*(N//2)+one*(N%2)
print(ans)