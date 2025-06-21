def main():
    a,b = map(int, input().split())
    n = (b-a+1)#要素数
    k = n//2

    if n%2==0:
        if a%2==0:
            if k%2==0:
                res = 0
            else:
                res =1
        else:
            k = (n-2)//2
            if k%2 == 1:
                res=(a^b^1)
            else:
                res = a^b
    else:
        if a%2 == 0:
            if k%2 == 0:
                res = (b)
            else:
                res = b^1
        else:
            if k%2==1:
                res = a^1
            else:
                res = a
    print(res)





if __name__ == '__main__':
    main()
