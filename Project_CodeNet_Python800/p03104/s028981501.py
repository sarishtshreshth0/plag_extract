def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

MAX_L = 43

def main():
    A, B = ZZ()

    p = []
    e = 1
    for _ in range(MAX_L+1):
        p.append(e)
        e *= 2

    def bitc(num):
        ret = []
        for i in range(1, MAX_L+1):
            x = (num//p[i]) * p[i-1] + max(0, num%p[i]-p[i-1]+1)
            ret.append(x%2)
        return ret

    a = bitc(max(0, A-1))
    b = bitc(B)
    output = 0
    for i in range(MAX_L): output += (a[i]+b[i])%2 * p[i]
    print(output)

    return

if __name__ == '__main__':
    main()
