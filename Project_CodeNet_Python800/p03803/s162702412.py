i = [int(s) for s in input().split()]
alice = i[0]
bob = i[1]

if alice == bob:
    print("Draw")
elif alice == 1:
    print("Alice")
elif bob == 1:
    print("Bob")
elif bob < alice:
    print("Alice")
else:
    print("Bob")
