#!/usr/bin/env python3

def II(): return int(input())
def MII(): return map(int, input().split())
def LII(): return list(map(int, input().split()))

def main():
    N = II()
    CSF = []
    for _ in range(N-1):
        c, s, f = MII()
        CSF.append((c, s, f))

    for i in range(N-1):
        t = 0
        for j, (c, s, f) in enumerate(CSF[i:]):
            if j == 0:
                t += s + c
            else:
                if t < s:
                    t += s - t 
                else:
                    if (t - s) % f != 0: 
                        t = ((t - s) // f + 1) * f + s
                t += c
        print(t)
    print(0)

if __name__ == '__main__':
    main()
