from collections import deque, Counter
N = int(input())
num_357 = [3, 5, 7]
dq = deque(num_357)
while dq:
    x = dq.popleft()
    if x <= 10**9:
        num_357.append(int(str(x) + "3"))
        num_357.append(int(str(x) + "5"))
        num_357.append(int(str(x) + "7"))
        dq.append(int(str(x) + "3"))
        dq.append(int(str(x) + "5"))
        dq.append(int(str(x) + "7"))

ans = 0
for num in num_357:
    if num <= N:
        c = {3: 0, 5: 0, 7: 0}
        for i in range(len(str(num))):
            if str(num)[i] == "3":
                c[3] += 1
            elif str(num)[i] == "5":
                c[5] += 1
            elif str(num)[i] == "7":
                c[7] += 1
        if c[3] >= 1 and c[5] >= 1 and c[7] >= 1:
            ans += 1
print(ans)
