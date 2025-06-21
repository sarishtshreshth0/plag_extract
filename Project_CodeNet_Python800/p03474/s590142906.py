def main():
    a, b = map(int, input().split())
    s = input()
    all_l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    hyphen = ['-']

    answer = 'Yes'
    for i in range(len(s)):
        if i == a:
            if s[i] not in hyphen:
                answer = 'No'
        else:
            if s[i] not in all_l:
                answer = 'No'

    print(answer)


if __name__ == "__main__":
    main()
