sus = ['0','1','2','3','4','5','6','7','8','9']
def base_sus(dig,n):
    if dig == 0: return ""
    return sus[dig%n]+base_sus(dig//n,n)
a,b = map(int,input().split())
print(len(base_sus(a,b)))