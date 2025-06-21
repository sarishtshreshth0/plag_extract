#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def main():
    a,b = map(int,input().split())
    s = input().rstrip()
    if len(s)==a+b+1:
        if s[a]=="-" and s.count("-")==1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__=="__main__":
    main()