n = int(input())

def dfs(x):
  check(x) # x が満たされているか確認する関数
  if x <= 100000000:
    dfs(10*x+3)
    dfs(10*x+5)
    dfs(10*x+7)
target = []
def check(x):
  if '3' in str(x) and '5' in str(x) and '7' in str(x):
    target.append(x)

dfs(0)

result = 0
for i in target:
  if i <= n:
    result+= 1

print(result)
