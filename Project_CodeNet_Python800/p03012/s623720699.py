#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]


n = int(input())
w = list(map(int, input().split()))

total = sum(w)
sa = []
for i in range(n):
    #print(w[0:i+1])
    #print(w[i+1:n+1])
    s1 = sum(w[0:i+1])
    s2 = total - s1
    sa.append(abs(s1-s2))
#print(sa)
print(min(sa))
