N = int(input())
Cs = []
Ss = []
Fs = []
for i in range(N-1):
    c, s, f = map(int, input().split())
    Cs.append(c)
    Ss.append(s)
    Fs.append(f)

for start in range(N):
    time = 0
    current_i = start
    while current_i < N-1:
        if time >= Ss[current_i]:
            if time % Fs[current_i] == 0:
                time += Cs[current_i]
                current_i += 1
            else:
                time = Fs[current_i] * (time // Fs[current_i] + 1)
        else:
            time = Ss[current_i]

    print(time)
