def ABC_80_B():
    N=input()
    N1=list(N)
    x=0
    for i in range(len(N1)):
        x+=int(N1[i])

    if int(N)%x==0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':

    ABC_80_B()