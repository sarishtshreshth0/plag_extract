def main():
    s = input()
    tmp1 = 0
    tmp2 = 0
    mae = 0

    for i in range(len(s)):
        if s[i] == mae:
            tmp1 += 1
            if s[i] == "0":
                mae = "1"
            else:
                mae = "0"
        else:
            if s[i] == "0":
                mae = "0"
            else:
                mae = "1"

    mae = 1

    for i in range(len(s)):
        if s[i] == mae:
            tmp2 += 1
            if s[i] == "0":
                mae = "1"
            else:
                mae = "0"
        else:
            if s[i] == "0":
                mae = "0"
            else:
                mae = "1"
    
    print(min(tmp1, tmp2))


if __name__ == "__main__":
    main()