def main():
  N, M = list(map(lambda a: int(a), input().split(" ")))

  if N >= M:
    print(0)
    return 0
  
  X = list(map(lambda x: int(x), input().split(" ")))
  X.sort()
  D = [X[i+1] - X[i] for i in range(len(X) - 1)]
  D.sort()
  print(sum(D[:M-N]))

main()