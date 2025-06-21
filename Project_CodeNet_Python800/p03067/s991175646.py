arr = list(map(int, input().split()))
c = arr[2]
arr.sort()
if c == arr[1]:
    print('Yes')
else:
    print('No')