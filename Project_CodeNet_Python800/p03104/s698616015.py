a,b = map(int, input().split())
if a%2:
    if (b-a)%2:
        print((( (b-a-1) // 2) % 2) *1 ^ a ^ b)
    else:
        print((( (b-a) // 2) % 2) *1 ^ a)
else:
    if (b-a+1)%2:
        print((( (b-a) // 2) % 2) *1 ^ b)
    else:
        print((( (b-a+1) // 2) % 2) *1)