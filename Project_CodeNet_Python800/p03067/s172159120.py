A, B, C = map(int, input().split())
V = sorted([A, B, C])
ans = 'Yes' if V[1] == C else 'No'
print(ans)
