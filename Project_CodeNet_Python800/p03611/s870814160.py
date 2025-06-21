n = int(input())
a = list(map(int, input().split()))

def func(a):
  count = [0] * (max(a)+1)

  for i in a:
      count[i] += 1

  max_n = 0
  for j in range(1, len(count)-1):
      max_n = max(max_n, count[j] + count[j-1] + count[j+1])
  max_n = max(max_n, count[-1] + count[-2])

  return max_n

print(n if len(set(a)) == 1 else func(a))
