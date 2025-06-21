N = [int(e) for e in input().split()]
if(N[0] == N[1]):
    print('Draw')
elif(N[0] == 1):
    print('Alice')
elif(N[1] == 1):
    print('Bob')
elif(N[0] > N[1]):
    print('Alice')
else:
    print('Bob')