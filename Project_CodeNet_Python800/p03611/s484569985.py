import collections

def main():
  N = int(input())
  A = [int(a) for a in input().split(" ")]
  CA = collections.Counter(A)
  minA = min(A)
  maxA = max(A)
  X = [CA[i] for i in range(minA, maxA + 1)]
  if len(X) == 1:
    print(X[0])
    return 0
  if len(X) == 2:
    print(X[0] + X[1])
    return 0
    
  Y = [X[j] + X[j+1] + X[j+2] for j in range(len(X) - 2)]
  print(max(Y))

main()