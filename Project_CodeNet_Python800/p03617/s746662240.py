Q, H, S, D = map(int, input().split())
L = int(input())
quantities = [(8*Q, 'Q'), (4*H, 'H'), (2*S, 'S'), (D, 'D')]
rest = {'Q': 4*Q, 'H': 2*H, 'S': S, 'D': D//2}
quantities.sort()
if quantities[0][1] == 'D' and L%2 != 0:
  print(L//2*D + rest[quantities[1][1]])
elif quantities[0][1] == 'D' and L%2 == 0:
  print(L//2*D)
else:
  print(L*rest[quantities[0][1]])