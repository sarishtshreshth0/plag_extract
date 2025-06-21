m_num = int(input())
w = list(map(int,input().split()))

temp = []
for i in range(m_num -1 ):
    temp.append(abs(sum(w[0:i+1]) - sum(w[i + 1:])))
print(min(temp))
