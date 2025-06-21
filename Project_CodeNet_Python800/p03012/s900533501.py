#!/usr/bin/env python3

# input = stdin.readline



def main():
  N = int(input())
  w = list(map(int,input().split()))
  def solve(w):
    res = 10**6
    s1 = 0
    s2 = sum(w)
    for i in range(len(w)):
      s1 += w[i]
      s2 -= w[i]
      res = min(res,abs(s1-s2))
    return res
  print(solve(w))
  return

if __name__ == '__main__':
  main()
