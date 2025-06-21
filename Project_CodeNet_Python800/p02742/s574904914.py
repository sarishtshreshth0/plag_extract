#B - Bishop △(TLE,WA)
H,W = map(int,input().split())

count = 0
if H == 1 or W == 1:#コーナーケース(H,Wが1の時どこにも動けない)
    count = 1
elif H % 2 == 0:
    count = (H // 2)*W
else :
    count = (H // 2)*W + ((W + 2 - 1) // 2)#x/yの切り上げ:(x+y-1)//y
print(count)