import math
def main():
  n = int(input())
  w = [input() for i in range(n)]
  flg=0
  
  for i in range(1,n):
    if w[i][0]!=w[i-1][len(w[i-1])-1]:
      flg=1
      break

  if flg==1 or len(set(w))!=n:
    print("No")
  else:
    print("Yes")
main()

