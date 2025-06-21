import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())


N = I()
CSF = [tuple(MI()) for i_ in range(N-1)]

for i in range(N):
    time = 0
    for j in range(i,N-1):
        c,s,f = CSF[j]
        if time < s:
            time = s
        else:
            time = s+f*((time-s+f-1)//f)
        time += c
    print(time)
