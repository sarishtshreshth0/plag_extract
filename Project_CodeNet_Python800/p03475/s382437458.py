n = int(input())
csf = [list(map(int,input().split())) for _ in range(n-1)]

ans = [0]*(n)
ans[n-2] = csf[n-2][0] + csf[n-2][1] # go to the goal.
# print('ans', ans)
for i in range(n-3, -1, -1):
    # print('i =',i)
    ans_cur = csf[i][0] + csf[i][1] # go to the next station with 1st train. 
    for j in range(i+1, n-1):
        # print('j = ', j)
        if ans_cur < csf[j][1]: # arrive before 1st train.
            ans[i] = ans[j]
            break
        while ans_cur%csf[j][2] != 0:
            ans_cur += 1 # wait for next train.
        ans_cur += csf[j][0]
    else:
        ans[i] = ans_cur

for val in ans:
    print(val)

    



