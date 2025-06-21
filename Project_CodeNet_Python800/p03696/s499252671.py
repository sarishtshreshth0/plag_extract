n = int(input())
s = input()
st=0
m=0
lv = 0
for x in s:
    if x == '(':
        lv+=1
    else:
        lv-=1
    m=min(m,lv)
gl=lv-m
st-=m
print('('*st+s+')'*gl)

