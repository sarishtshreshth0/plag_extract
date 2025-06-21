n = int(input())
l = [input() for _ in range(n)]
flg1 = len(l) == len(set(l))
flg2 = all(l[i][-1] == l[i + 1][0] for i in range(n - 1))
print(["No", "Yes"][flg1 and flg2])
