def main():
    s = input()
    if len(s) < 4 or "YAKI" != s[:4]:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()