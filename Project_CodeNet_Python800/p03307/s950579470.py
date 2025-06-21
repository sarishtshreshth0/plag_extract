def main():
    a, b = 2, int(input())
    ta, tb = a, b
    if b == 0: print(0)
    while a%b != 0:
       a, b = b, a%b
    print(int((ta*tb)/b))
main()