import sys
def I(): return int(sys.stdin.readline().rstrip())


N = I()
divisor = []
for i in range(int(N**.5),0,-1):
    if N % i == 0:
        if i != N//i:
            print(max(len(str(i)),len(str(N//i))))
        else:
            print(len(str(i)))
        break
