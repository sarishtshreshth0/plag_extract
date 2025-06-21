def main():
  N = int(input())
  S = list(str(input()))
  num_1 = 0
  num_2 = 0
  for i in range(N):
    if S[i] == '(':
      num_1 += 1
    else:
      if num_1 > 0: num_1 -= 1
  for i in range(N-1, -1, -1):
    if S[i] == ')':
      num_2 += 1
    else:
      if num_2 > 0: num_2-=1
  for i in range(num_1):
    S.append(')')
  for i in range(num_2):
    S.insert(0, '(')
  print(''.join(S))

if __name__ == "__main__":
  main()