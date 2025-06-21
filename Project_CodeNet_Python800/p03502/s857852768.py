N_str = input()
N = int(N_str)

if N % sum([int(s) for s in N_str]) == 0:
    print("Yes")
else:
    print("No")