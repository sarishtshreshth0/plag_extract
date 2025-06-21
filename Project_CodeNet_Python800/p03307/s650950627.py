#2019/10/10
N = int(open(0).read())
i = 0
while(N*i <= 10**9):
    i+=1
    #print(i)
    if (N*i)%2 == 0:
        print(N*i)
        break