def mainFunc():
    M, D = list(map(int, input().split(" ")))
    months = []
    for i in range(10, D + 1):
        s = str(i).zfill(2)
        divD = list(map(int, list(s)))
        ml = divD[0] * divD[1]
        if 1 <= ml <= M and divD[0] > 1 and divD[1] > 1:
            months.append(ml)
    
    print(len(months))

mainFunc()