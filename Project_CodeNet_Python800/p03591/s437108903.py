

def main():
    s = input()
    if len(s) >= 4:
        if s[0:4] == "YAKI":
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
