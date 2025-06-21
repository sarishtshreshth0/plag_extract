import math
def main():
  M,D = map(int,input().split())
  if D < 22:
       print(0)
       return
  cnt = 0
  for i in range(D + 1):
      if 2 <= (i/10) and 2 <= (i%10) and math.floor(i/10)*(i%10) <= M:
          cnt += 1
  print(cnt)
  
main()