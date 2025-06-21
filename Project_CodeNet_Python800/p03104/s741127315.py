def main():
    A, B = map(int, input().split())

    def xor_world(k):
        """[0,k]"""
        r = k % 4
        if r == 0:
            return k
        elif r == 1:
            return 1
        elif r == 2:
            return 1 ^ k
        else:
            return 0

    ans = xor_world(B) ^ xor_world(A) ^ A
    print(ans)


if __name__ == '__main__':
    main()
