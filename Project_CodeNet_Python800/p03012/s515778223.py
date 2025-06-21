def main():
  n = int(input())
  wlist = list(map(int, input().split()))
  min_diff = float('inf')
  for i in range(1, n):
    s1 = sum(wlist[:i])
    s2 = sum(wlist[i:])
    diff = abs(s1-s2)
    if min_diff > diff:
      min_diff = diff
  print(min_diff)
main()