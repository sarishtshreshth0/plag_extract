from sys import stdin
input = stdin.readline


def main():
  N = int(input())
  S = input()[:-1]

  pre = S[0]
  cnt = 1
  for i in range(1, N):
    if pre == S[i]:
      pre = S[i]
      continue
    cnt += 1
    pre = S[i]
  print(cnt)


if(__name__ == '__main__'):
  main()
