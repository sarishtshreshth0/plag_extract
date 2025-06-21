import sys
N = int(input())
lst = [str(input()) for _ in range(N)]


if len(set(lst)) != N:
    print('No')
    sys.exit()

for i in range(len(lst)-1):
    if lst[i][-1] != lst[i+1][0]:
        print('No')
        sys.exit()
print('Yes')