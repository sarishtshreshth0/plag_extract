def main():
    #n = int(input())
    a,b,c,d = map( int, input().split())
    if c>=b or a>=d:
        print(0)
    elif a<=c and b>=d:
        print(d-c)
    elif c<=a and d>=b:
        print(b-a)
    elif a >= c:
        print(d-a)
    elif c >= a:
        print(b-c)
    
    
if __name__ == '__main__':
    main()