#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    words=[]
    n = int(input())
    words=[input().rstrip() for _ in range(n)]

    if len(set(words))!=n:
        print("No")
        exit()

    endstring=""
    for word in words:
        if len(endstring)==0:
            endstring=word[-1]
        else:
            if endstring==word[0]:
                endstring=word[-1]
            else:
                print("No")
                exit()
    print("Yes")


if __name__=="__main__":
    main()