x = int(input())
cnt = 0

m_500 = x // 500
m_5 = (x - m_500*500) // 5

print(m_500*1000 + m_5*5)