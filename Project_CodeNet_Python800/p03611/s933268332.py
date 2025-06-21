n = int(input())
ls = list(map(int,input().split()))
di = [0]*(max(ls)+3)
for i in ls:
    di[i] += 1
    di[i+1] += 1
    di[i+2] += 1
print(max(di))