def main():
    A, B, C = map(int, input().split())
    A, B = sorted([A, B])

    if A <= C <= B:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()