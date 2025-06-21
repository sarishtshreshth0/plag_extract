n = int(input())
w = [input() for i in range(n)]
cnt = 0
for j in range(n-1):
    if (w[j][-1] == w[j+1][0])&(w.count(w[j])==1):
        pass
    else:
        cnt += 1
print("No") if cnt else print("Yes")