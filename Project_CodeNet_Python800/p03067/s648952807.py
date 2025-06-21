A, B, C = map(int, input().split())

# normalize
norm_A = 0
norm_B = B - A
norm_C = C - A

print('Yes' if abs(norm_B) >= abs(norm_C) and (norm_B * norm_C) > 0 else 'No')
