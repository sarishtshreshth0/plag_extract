S = input()
print('Yes') if S[:min(4, len(S))] == 'YAKI' else print('No')