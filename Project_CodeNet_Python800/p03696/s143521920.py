def cin():  return list(map(int,input().split()))

N = cin()[0]
S = input()

tmp = S[::]
for i in range(100): tmp = tmp.replace("()", "")
cnt1 = 0
cnt2 = 0
for i in range(len(tmp)):
    if tmp[i] == '(': cnt1 += 1
    else: cnt2 += 1

ans = S[::]
ans = "(" * cnt2 + S + ')' * cnt1;
print(ans);