A, B, C = map(int, input().split())

if A<B:
    a = A
    b = B
else:
    a = B
    b = A


print('Yes') if a<=C<=b else print('No')
