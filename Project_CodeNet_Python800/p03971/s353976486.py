n, a, b = map(int, input().split())
s = list(input())

result = []
cnt = 0
cnt_b = 0
limit = a + b

for student in s:
    if student == "c":
        result.append("No")
    elif (student == "a") & (cnt < limit):
        result.append("Yes")
        cnt += 1
    elif (student == "b") & (cnt < limit) & (cnt_b < b):
        result.append("Yes")
        cnt += 1
        cnt_b += 1
    else:
        result.append("No")
print("\n".join(result))