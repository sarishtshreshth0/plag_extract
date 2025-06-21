n = input()
print(['No', 'Yes'][int(int(n) % sum([int(x) for x in n]) == 0)])
