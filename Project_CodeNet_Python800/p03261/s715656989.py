N = int(input())
word_bank = set()
last_char = ''

for n in range(N):
  new_word = input()
  if new_word in word_bank:
    print('No')
    exit(0)
  elif n != 0 and new_word[0] != last_char:
    print('No')
    exit(0)
  else:
    word_bank.add(new_word)
    last_char = new_word[-1]

print('Yes')