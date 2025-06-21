S = input()
S_odd = S[1::2]
S_even = S[0::2]

oddlist = []
evenlist = []

for i in range(len(S_odd)):
    oddlist.append(int(S_odd[i]))
for i in range(len(S_even)):
    evenlist.append(int(S_even[i]))

EvenSum = sum(evenlist)
OddSum = sum(oddlist)


if EvenSum <= OddSum:
    ans = len(oddlist) - OddSum
    ans += EvenSum
else:
    ans = len(evenlist) - EvenSum
    ans += OddSum

print(ans)