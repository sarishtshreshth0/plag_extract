Q, H, S, D = map(int, input().split())
N = int(input())
cheap_l = min(4*Q, 2*H, S)
print(min(N*cheap_l, (N//2)*D+(N%2)*cheap_l))