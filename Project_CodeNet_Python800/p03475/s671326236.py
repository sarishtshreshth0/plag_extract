n = int(input())
csf = [list(map(int, input().split())) for _ in range(n-1)]

def time(m):
    c, s, f = csf[m-1]
    depart_next = s
    arrive_next = s+c
    while m < n-1:
        nc, ns, nf = csf[m]
        i = 0
        while ns + nf*i < arrive_next:
            i += 1
        depart_next = ns + nf*i
        arrive_next = depart_next + nc
        m += 1
    return arrive_next


for i in range(1, n):
    print(time(i))
print(0)
