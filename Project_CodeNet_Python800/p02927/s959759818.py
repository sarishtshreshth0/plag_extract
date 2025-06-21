M,D = map(int,input().split())
if D<=21:
    print(0)
else:
    D10 = D//10
    D1 = D%10
    cnt = 0
    for i in range(2,D10+1):
       for j in range(2,10):
           if i*10 + j > D:
               break
           if 1 <= i*j <= M:
               cnt += 1
    print(cnt)           