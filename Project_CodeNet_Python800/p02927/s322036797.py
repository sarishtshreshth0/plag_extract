def main():
    month, day = map(int, input().split())
    answer = 0
    for m in range(1, month + 1):
        for d in range(1, day + 1):
            if (d % 10) * (d // 10) == m and (d % 10) > 1 and (d // 10) > 1:
                answer += 1
    print(answer)


if __name__ == '__main__':
    main()

