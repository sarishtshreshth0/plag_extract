def main():

    A, B, C = map(int, input().split())
    if A < C < B or B < C < A:
        return "Yes"
    return "No"

if __name__ == '__main__':
    print(main())