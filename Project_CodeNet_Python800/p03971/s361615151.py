'''
Created on 2020/08/19

@author: harurun
'''
def main():
  import sys
  pin=sys.stdin.readline
  pout=sys.stdout.write
  perr=sys.stderr.write

  N,A,B=map(int,pin().split())
  S=pin()[:-1]
  cnt=0
  cn=0
  for i in range(N):
    if S[i]=="a" and cnt<A+B:
      cnt+=1
      print("Yes")
    elif S[i]=="b" and cnt<A+B and cn<B:
      cnt+=1
      cn+=1
      print("Yes")
    else:
      print("No")
  return 

main()
