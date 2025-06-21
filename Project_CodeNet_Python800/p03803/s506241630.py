
a,b=map(int,input().split())

list=[2,3,4,5,6,7,8,9,10,11,12,13,1]
# print(list.index())

a_val=list.index(a)
b_val=list.index(b)

if a_val>b_val:print('Alice')
elif a_val<b_val:print('Bob')
else:print('Draw')