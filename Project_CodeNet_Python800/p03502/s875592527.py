import math
def main():
  n = int(input())
  x=n
  fx=0
  while x>0:
    fx+=x%10
    x=int(x/10)
  if n%fx==0:
    print('Yes')
  else:
    print('No')
main()
