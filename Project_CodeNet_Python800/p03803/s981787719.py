A,B=map(int,input().split())

def judge(a,b):
  if a > b > 1 or (a == 1 and b != 1):
    return "Alice"
  elif a == b:
    return "Draw"
  else:
    return "Bob"
  
print(judge(A,B))
