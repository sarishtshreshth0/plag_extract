# 第一回日本最強プログラマー学生選手権-予選-: A – Takahashi Calendar
M, D = [int(i) for i in input().split()]

seki_no_hi = 0

for m in range(1, M + 1):
    for d in range(10, D + 1):
        d1 = d % 10
        d10 = d // 10
        if d1 >= 2 and d10 >= 2 and d1 * d10 == m:
            seki_no_hi += 1

print(seki_no_hi)