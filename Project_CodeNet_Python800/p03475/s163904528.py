import math
def main():
  N = int(input())
  ans = [0] * N
  for i in range(N-1):
    c, s, f = map(int, input().split())
    for j in range(i + 1):
      ans[j] = f*max(math.ceil(ans[j]/f), math.ceil(s/f))+c
  for i in range(N):
    print(ans[i])
if __name__ == "__main__":
  main()