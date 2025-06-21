def main():
    n = int(input())
    s = input()
    left = 0
    right = 0
    for i in range(n):
        if s[i] == '(':
            right += 1
        else:
            if right == 0:
                left += 1
            else:
                right -= 1
    print('('*left+s+')'*right)

if __name__ == '__main__':
    main()
