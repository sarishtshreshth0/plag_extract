def main():
    n = int(input())
    n_f = n
    f = 0
    for i in range(8):
        if n >= 10: 
            f += n % 10
            n  = n // 10
        else:
            f += n % 10
            break
    if n_f % f == 0:
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    main()
    
