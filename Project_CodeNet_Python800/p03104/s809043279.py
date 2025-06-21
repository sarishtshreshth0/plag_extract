a, b = map(int, input().split())
if a == b:
    print(a)
else:
    bits = []
    for i in range(b.bit_length()):
        k = pow(2, i+1)
        nb, rb = divmod(b, k)
        na, ra = divmod(max(0,a-1), k)

        bb = nb*(k//2) + max(0, rb - k//2 + 1)
        aa = na*(k//2) + max(0, ra - k//2 + 1)
        bits.append((bb-aa)%2)
    # print(bits)
    print(int(''.join(map(str, bits[::-1])), 2))
