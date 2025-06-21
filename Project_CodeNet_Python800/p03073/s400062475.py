import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = list(input())
    zero, one = 0, 0
    for i in range(len(s)):
        if i%2 == 0:
            if s[i] == '1':
                zero += 1
            else:
                one += 1
        else:
            if s[i] == '1':
                one += 1
            else:
                zero += 1
    print(min(zero, one))
        
if __name__ == '__main__':
    main()