A, B, C = map(int, input().split())
print(('No', 'Yes')[(A < C and C < B) or (B < C and C < A)])