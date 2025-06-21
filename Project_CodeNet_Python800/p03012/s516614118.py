n = int(input())
weight = list(map(int,input().split()))
minimum_weight = abs(sum(weight[0:1]) - sum(weight[1:n+1]))

for i in range(1,n-1):
  minimum_weight = min(minimum_weight, abs(sum(weight[0:i+1]) - sum(weight[i+1:n+1])))
  
print(minimum_weight)