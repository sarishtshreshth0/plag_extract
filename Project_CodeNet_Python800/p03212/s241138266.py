n = int(input())

cnt = 0
L = ["3","5","7"]
def migona(x):
    global cnt
    if int(x) > n:
        return
    if all(str(int(x)).count(i) > 0 for i in "357"):
        cnt +=1
        #print(x)
    
    migona(x+"3")
    migona(x+"5")
    migona(x+"7")
    
    return

migona("0")
print(cnt)