N = int(input())
pre = input()
dict = {pre:1}
for i in range(N-1):
    now = input()
    if now[0]!=pre[-1]:
        print('No')
        exit(0)
    elif now in dict:
        print('No')
        exit(0)
    else:
        dict[now] = 1
        pre = now 
print('Yes')