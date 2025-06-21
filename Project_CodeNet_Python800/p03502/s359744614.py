n = input()

n_sum = 0
for i in range(len(n)):
  n_sum += int(n[i])

print('Yes' if int(n)%n_sum == 0 else 'No')