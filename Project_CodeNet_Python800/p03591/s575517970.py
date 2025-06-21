def main():
    s = input().rstrip()
    if len(s) >= 4 and s[:4] == "YAKI":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
