N = int(input())
dia = []
for _ in range(N-1):
    dia.append(list(map(int, input().split())))

def to_next(start_time, sta):
    
    time = 0
    if dia[sta][1] > start_time:
        time += dia[sta][1] - start_time
    elif start_time % dia[sta][2] != 0:
        time += dia[sta][2] * (start_time // dia[sta][2] + 1) - start_time
    time += dia[sta][0]
    return time

def to_end(sta):
    time = 0
    while sta != N-1:
        time += to_next(time, sta)
        sta += 1
    return time
for i in range(N - 1):
    print(to_end(i))
print(0)