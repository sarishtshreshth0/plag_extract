def check():
    N = input()
    if int(N)%sum(map(int,list(N)))==0:
        return 'Yes'
    return 'No'
print(check())