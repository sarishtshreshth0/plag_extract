x = int(input())
g_happy = 0

# 500で割った商*1000happy
g_happy += 1000 * (x // 500)
# 500で割った商*500をｘから引く
x -= 500 * (x // 500)
# 5で割った商*5happy
g_happy += 5 * (x // 5)
print(g_happy)