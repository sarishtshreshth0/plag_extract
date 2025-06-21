num = int(input())
weight = list(map(int, input().split()))

d = []
for i in range(len(weight)):
  d.append(abs(sum(weight[:i])-sum(weight[i:])))
  
print(min(d))