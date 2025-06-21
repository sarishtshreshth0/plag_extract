S = input()
cnt = sum(i % 2 == 0 and s == "1" or i % 2 == 1 and s == "0" for i, s in enumerate(S))
print(min(cnt, len(S) - cnt))