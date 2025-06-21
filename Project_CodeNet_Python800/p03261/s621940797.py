def main():
    w=[input() for _ in range(int(input()))]
    sumi=set()
    p=w[0][0]
    for s in w:
        if s in sumi or p != s[0]:
            print("No")
            return
        sumi.add(s)
        p = s[-1]
    print("Yes")
    
if __name__ == "__main__":
    main()