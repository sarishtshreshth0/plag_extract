def main():
    N = int(input())
    W_before = input()
    word_set = set()
    word_set.add(W_before)
    for i in range(N-1):
        W_after = input()
        if W_before[-1] != W_after[0]:
            print('No')
            return
        if W_after in word_set:
            print('No')
            return
        word_set.add(W_after)
        W_before = W_after
    print('Yes')

if __name__ == "__main__":
    main()
