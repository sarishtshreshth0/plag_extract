from sys import stdin

'''
def answer(A, x, y):
    if A < y < x:
        print("Yes")
    else:
        print("No")
'''


def main():
    A, B, C = [int(x) for x in stdin.readline().split()]
    if A < B:
        if A < C < B:
            print("Yes")
        else:
            print("No")
    else:
        if B < C < A:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
