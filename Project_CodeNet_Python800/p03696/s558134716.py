from collections import deque


def main():
    n = int(input())
    s = input()
    left = 0
    stack = deque([])
    for ss in s:
        if ss == "(":
            stack.append("(")
        elif not stack:
            left += 1
        else:
            stack.pop()
    print(left * "(" + s + len(stack) * ")")


if __name__ == '__main__':
    main()

