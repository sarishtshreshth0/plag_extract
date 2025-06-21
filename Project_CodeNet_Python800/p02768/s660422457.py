def factorial(a,n):
  # n*(n-1)*,,,,,*(n-a+1)
  ans=1
  for i in range(n,n-a,-1):
    ans=(ans*i)%M
  return ans


def pow(x, n):
  ans=1
  while n:
    if n % 2 == 1:
      ans = (ans*x)%M
    x = (x*x)%M
    n >>= 1
  return ans


def main():
  ans=pow(2,N) - 1
  ans-=(factorial(A,N)*pow(factorial(A,A),M-2))%M
  ans+= 0 if ans>=0 else M
  ans-=(factorial(B,N)*pow(factorial(B,B),M-2))%M
  print(ans if ans>=0 else ans+M)
  
  
if __name__=='__main__':
  N, A, B = map(int, input().split())
  M = 10**9 + 7
  main()
