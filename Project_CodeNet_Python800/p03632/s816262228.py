import math

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    A, B, C, D = mi()
    print(len(set(range(A, B))&set(range(C, D))))

if __name__ == '__main__':
    main()