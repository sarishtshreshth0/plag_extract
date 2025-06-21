def resolve():
  n = input()
  x = int(n)
  fx = 0
  for c in n:
    fx += int(c)
  if x % fx == 0:
    print('Yes')
  else:
    print('No')

  return

if __name__ == "__main__":
  resolve()
