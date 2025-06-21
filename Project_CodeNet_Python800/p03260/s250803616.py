def main():
    line = input()
    a, b= [int(x) for x in line.split()]
    if a == 2 or b == 2:
        print('No')
    else:
        print('Yes')
main()