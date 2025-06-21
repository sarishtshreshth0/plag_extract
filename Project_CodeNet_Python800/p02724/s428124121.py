X = int(input())

ans=0

if X < 500:
    print((X // 5) * 5)
else:
    ans += (X // 500)*1000
    X -= (X//500)*500
    ans += (X//5)*5
    print(ans)

