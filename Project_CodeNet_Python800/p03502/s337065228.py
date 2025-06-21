def main():
    n = int(input())

    sum = 0

    for digit in str(n):
        sum += int(digit)
    
    if n % sum == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()