n_str = input()
print("Yes" if int(n_str) % sum([int(c) for c in n_str]) == 0 else "No")