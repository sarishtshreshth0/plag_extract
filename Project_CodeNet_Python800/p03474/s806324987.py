import sys
input = sys.stdin.readline


def main():
    integer = {"1","2","3","4","5","6","7","8","9","0"}
    a,b = [int(i) for i in input().strip().split()]
    s = input().strip()
    if len(s) != a + b + 1:
        print("No")
        return
    
    for n in s[:a]:
        if n not in integer:
            print("No")
            return
    if s[a] != "-":
        print("No")
        return
    for n in s[a + 2:]:
        if n not in integer:
            print("No")
            return
    
    print("Yes")
    return


if __name__ == "__main__":
    main()