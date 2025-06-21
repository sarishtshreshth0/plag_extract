def Base(X, n):
    if (int(X/n)):
        return Base(int(X/n), n)+str(X%n)
    return str(X%n)

def main():
  N, K = map(int, input().split())
  ans1 = Base(N, K)
  ans = len(ans1)
  print(ans)

main()