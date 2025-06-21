import sys
def input(): return sys.stdin.readline().strip()

def main():
    a, b = map(int, input().split())
    if a == 1: a += 13
    if b == 1: b += 13
    if a == b:
        print("Draw")
    elif a > b:
        print("Alice")
    else:
        print("Bob")

if __name__ == "__main__":
    main()
