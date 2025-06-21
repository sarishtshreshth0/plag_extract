def main():
    length = int(input())
    distance = list(map(int, input().split()))
    count_distance = {}
    for d in distance:
        if d in count_distance:
            count_distance[d] += 1
        else:
            count_distance[d] = 1
    count_distance = sorted(count_distance.items(), key=lambda x: x[0])
    answer = 0
    mod = 998244353
    if distance[0] == 0 and count_distance[0][1] == 1:
        answer = 1
        for i in range(1, len(count_distance)):
            if count_distance[i][0] == count_distance[i - 1][0] + 1:
                answer = (answer * pow(count_distance[i - 1][1], count_distance[i][1], mod)) % mod
            else:
                answer = 0
                break
    print(answer)


if __name__ == '__main__':
    main()

