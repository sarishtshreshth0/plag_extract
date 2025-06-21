#!/usr/bin/env python3


def main():
    n, a, b = map(int,input().split())
    s = input()
    sanka = 0
    sankaigai = 0

    for hito in s:
        if hito is "c":
            print("No")
        elif hito is "a":
            if sanka < a+b:
                print("Yes")
                sanka+=1
            else:
                print("No")
        elif hito is "b":
            if sanka < a+b:
                if sankaigai < b:
                    print("Yes")
                    sanka+=1
                    sankaigai+=1
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")


if __name__ == '__main__':
    main()