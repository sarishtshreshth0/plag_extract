def main():
    m,d = map(int,input().split())
    if d < 22 or m < 4:
        print(0)
        exit(0)
    cnt = 0
    for i in range(2,d//10+1):
        for j in range(2,10):
            if i*10 + j > d:
                break
            if i * j <= m:
                cnt += 1
    print(cnt)

if __name__ =="__main__":
    main()
