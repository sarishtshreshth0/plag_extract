import math

def main():
  N, K = map(int, input().split())
  i = 1
  tmp = 1
  
  while i > -1:
    if N >= K ** i:
      tmp += 1
    else:
      print(tmp)
      return
    
    i += 1
  
  
main()