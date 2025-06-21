mo = input().split()
shi = int(mo[1][0]) 
mo1 = [int(i) for i in mo]
if mo1[1] < 22:
    print (0)
else:
    cao = 0
    for i in range(2, mo1[0] + 1):
        for j in range(2, shi + 1):
            if i % j == 0:
                if i // j in range(2, 10) and ((j * 10 + i // j) <= mo1[1]):
                    cao += 1    
    print (cao)