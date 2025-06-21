Q,H,S,D = map(int, input().split())
N = int(input())

onelit = min((4*Q),(2*H),(S))

pattern1 = N * onelit
pattern2 = ((N//2)*D) + ((N%2) * onelit)

print(min(pattern1, pattern2))