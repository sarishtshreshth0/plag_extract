#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    h,w = map(int,input().split())
    if h==1 or w ==1:
        print(1)
        exit()
    flag=h*w
    if flag % 2 ==0:
        print(flag//2)
    else:
        print(int(flag/2)+1)

if __name__=="__main__":
    main()