def mips():
    return map(int,input().split())
def ii():
    return int(input())
N = ii()
L = []
for i in range(N-1):
    C,S,F = mips()
    L.append([C,S,F])
for i in range(N-1):
    x = L[i][0] + L[i][1]
    j = i + 1
    while j != N-1:
        if x >= L[j][1] and x % L[j][2] == 0: #no waiting time :)
            x += L[j][0]
            j += 1
        else:
            if x < L[j][1]: #1st train will arrive shortly ;)
                x += (L[j][1]-x + L[j][0])
                j += 1
            else: #if x % L[j][2] != 0, 1st train gone, wait for next :-(
                while x % L[j][2] != 0:
                    x += 1
                x += L[j][0] #a train arrived, go to next station.
                j += 1
    print(x)
print(0)