n = int(input())

word = [input()]
for _ in range(n-1):
  w = input()
  if w not in word and w[0] == word[-1][-1]: word.append(w)
  else:
    print("No")
    exit()
print("Yes")