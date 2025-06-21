S = input()
count = 0
for i,tile in enumerate(S):
    if i % 2 and tile == "0":
        count += 1
    if i % 2 == 0 and tile == "1":
        count += 1

ans = min(count, len(S) - count)
print(ans)
