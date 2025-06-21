N=int(input())

def digit(x):
    digit=1
    while x>0:
        if x//10>0:
            digit+=1
            x//=10
        else:
            break
    return digit

for i in range(int(N**(1/2)),-1,-1):
    if N%i!=0:
        pass
    else:
        print(digit(N//i))
        break

        
