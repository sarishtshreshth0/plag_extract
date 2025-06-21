def main():
    N = int(input())
    words = []
    record = []
    previous = ''
    for i in range(N):
        words.append(str(input()))
    for i in range(N):
        if i == 0:
            record.append(words[i])
            previous = words[i]
        elif not words[i] in record and previous[-1] == words[i][0] and i != 0:
            record.append(words[i])
            previous = words[i]
        else:
            print('No')
            return
    print('Yes')
main()  