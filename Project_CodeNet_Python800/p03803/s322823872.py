def main():
    a, b = map(int, input().split())
    power_list = [0, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    if power_list[a] > power_list[b]:
        print("Alice")
    elif power_list[a] < power_list[b]:
        print("Bob")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
