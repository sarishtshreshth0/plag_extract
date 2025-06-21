import math
n = int(input())

root = math.sqrt(n)
x = str(int(root // 1))
answer = 0

for i in reversed(range(1, int(x) + 1)):
    if n % i == 0:
        answer = i
        break
answer_2 = int(n / answer)

if len(str(answer)) >= len(str(answer_2)):
    print(len(str(answer)))
else:
    print(len(str(answer_2)))