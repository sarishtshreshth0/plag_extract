N = input()
a = list(map(int, input().split()))
answer = 0
a.sort()
a_count = [0 for _ in range(10 ** 5 + 10)]
for x in a:
  a_count[x] += 1
for i in range(1, 10 ** 5 + 5):
  answer = max(answer, a_count[i - 1] + a_count[i] + a_count[i + 1])
print(answer)