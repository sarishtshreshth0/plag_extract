n, a, b = [int(x) for x in input().split()]
s = input()

winners = []
foreign_winners = [0 for _ in range(len(s))]
winner_count = 0

foreign_score = 1
for i, c in enumerate(s):
  if c == 'b':
    foreign_winners[i] = foreign_score
    foreign_score += 1

for i, c in enumerate(s):
  if c == 'a':
    if winner_count < a+b:
      winners.append("Yes")
      winner_count += 1
    else:
      winners.append("No")
  elif c == 'b':
    if winner_count < a+b and foreign_winners[i] <= b:
      winners.append("Yes")
      winner_count += 1
    else:
      winners.append("No")
  else:
    winners.append("No")

for l in winners:
  print(l)