def main():
    a,b = map(int,input().split())
    answer = "No"
    for c in range(1,4):
        if a*b*c % 2 == 1:
            answer = "Yes"
            break

    print(answer)


if __name__ == '__main__':
    main()
