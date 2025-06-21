M, D = map(int, input().split())

# print("M:", M, "D:", D)

count = 0
# days = []

for m in range(1, M+1):
    for d in range(1, D+1):
        # print("m: ", m, " d: ", d, " d10: ", d/10, " d1", d%10)
        d1 = d % 10
        d10 = d // 10
        if (d1 * d10) == m and d1 != 1 and d10 != 1:
            # days.append("{}月{}日".format(m, d))
            count += 1

# for day in days:
#     print(day)
print(count)