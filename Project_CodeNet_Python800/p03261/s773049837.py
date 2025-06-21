N = int(input())
a_word = input()
words = [a_word]
judge = 'Yes'
for i in range(N-1):
  b_word = input()
  if not a_word[-1] == b_word[0]:
    judge = 'No'   
  elif b_word in words:
    judge = 'No'
  words.append(b_word)
  a_word = b_word

print(judge)