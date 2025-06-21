S = input()

S1 = S[0::2]
S2 = S[1::2]

S1_0 = S1.count("0")
S1_1 = S1.count("1")
S2_0 = S2.count("0")
S2_1 = S2.count("1")

#101010
ans1 = S1_0 + S2_1
#010101
ans2 = S1_1 + S2_0

print(min(ans1,ans2))