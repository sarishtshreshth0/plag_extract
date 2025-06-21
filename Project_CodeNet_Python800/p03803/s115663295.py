a,b=map(int,input().split())

def evaluate(x):
  if x != 1:
    return x
  return 14

a,b=map(evaluate,(a,b))

if a>b:print('Alice')
elif a==b:print('Draw')
else:print('Bob')