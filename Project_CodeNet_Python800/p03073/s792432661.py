S = input()
N = len(S)

ans1 = "".join(["1" if i%2 == 0 else "0" for i in range(N)])
ans2 = "".join(["0" if i%2 == 0 else "1" for i in range(N)])

print(min(bin(int(S, 2)^int(ans1, 2)).count("1"), bin(int(S, 2)^int(ans2, 2)).count("1")))