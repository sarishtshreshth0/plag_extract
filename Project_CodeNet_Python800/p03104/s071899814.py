A, B = map(int, input().split())
bin_A = bin(A - 1)
bin_B = bin(B)
A_xor = [0 for _ in range(len(bin_B) - 2)]
B_xor = [0 for _ in range(len(bin_B) - 2)]
for i in range(len(bin_B)):
    if i == 0:
        if B % 4 == 1 or B % 4 == 2:
            B_xor[i] = 1
    else:  
        if (B // pow(2, i)) % 2 == 1 and (B % pow(2, i)) % 2 == 0:
            B_xor[i] = 1
if A == 0:
    print(int("".join(map(str, B_xor[::-1])), 2))
    exit()
for i in range(len(bin_A)):
    if i == 0:
        if (A - 1) % 4 == 1 or (A - 1) % 4 == 2:
            A_xor[i] = 1
    else:
        if ((A - 1) // pow(2, i)) % 2 == 1 and ((A - 1) % pow(2, i)) % 2 == 0:
            A_xor[i] = 1
ans = []
for a, b in zip(A_xor, B_xor):
    if a != b:
        ans.append(1)
    else:
        ans.append(0)
print(int("".join(map(str, ans[::-1])), 2))