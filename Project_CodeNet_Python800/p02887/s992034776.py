import itertools
a=int(input())
b=input()

list2 = [k for k, v in itertools.groupby(b)]
print(len(list2))
