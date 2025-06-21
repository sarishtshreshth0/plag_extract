def main():
    word = input()
    print("Yes" if 4 <= len(word) and word[:4] == "YAKI" else "No")


if __name__ == '__main__':
    main()

