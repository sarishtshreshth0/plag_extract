def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    cuma = [0]
    for i in range(n):
        cuma.append(cuma[-1]+a[i])
    dict = {}
    for i in cuma:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    ans = 0    
    for i in dict:
        ans += dict[i]*(dict[i]-1)//2
    print(ans)
resolve()