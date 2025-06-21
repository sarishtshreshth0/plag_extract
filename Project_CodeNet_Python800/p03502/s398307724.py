if __name__ == '__main__':
    n = int(input())
    s = str(n)
    sum=0
    for i in s:
        sum+= int(i)

    if n%sum ==0:
        print("Yes")
    else:
        print("No")