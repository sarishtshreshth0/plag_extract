import sys
def input(): return sys.stdin.readline().strip()

def f(a, n): # (1\xor 2\xor ...\xor a) のnビット目の値
    if a == 0: return 0
    if n == 0 and (a % 4 == 0 or a % 4 == 3): return 0
    if n == 0 and (a % 4 == 1 or a % 4 == 2): return 1
    idx = a // (2 ** n)
    if idx % 2 == 0: return 0
    return (a - idx * 2**n + 1) % 2

def g(a, b, n): # (a\xor a+1\xor...\xor b)のnビット目の値
    if a == 0: return f(b, n)
    return (f(b, n) + f(a-1, n)) % 2


def main():
    A, B = map(int, input().split())
    ans = 0
    for i in range(41):
        ans += g(A, B, i) * 2**i
        #print("i={}, 1-{}->{}, 1-{}->{} --> g={}".format(i, B, f(B, i), A-1, f(A-1, i), g(A, B, i)))
    print(ans)


if __name__ == "__main__":
    main()
