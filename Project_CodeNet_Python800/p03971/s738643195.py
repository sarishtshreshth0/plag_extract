import math


def resolve():
    import sys
    input = sys.stdin.readline
    row1 = [int(x) for x in input().rstrip().split(" ")]
    # row2 = [int(x) for x in input().rstrip().split(" ")]
    s = input().rstrip()

    n = row1[0]
    a = row1[1]
    b = row1[2]

    kokunai = 0
    kaigai = 0
    for char in s:
        if char == "a":
            if(kaigai + kokunai < a + b):
                print("Yes")
                kokunai += 1
                continue

        elif char == "b":
            if((kaigai + kokunai < a + b) and (kaigai < b)):
                print("Yes")
                kaigai += 1
                continue
        print("No")








if __name__ == "__main__":
    resolve()
