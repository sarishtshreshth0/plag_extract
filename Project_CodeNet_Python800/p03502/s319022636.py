s = input()
l = [int(a) for a in s]
print(["No", "Yes"][int(s) % sum(l) == 0])