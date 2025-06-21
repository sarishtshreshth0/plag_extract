a,b=map(int,input().split())
num=[2,3,4,5,6,7,8,9,10,11,12,13,1]
print('Alice'if num.index(a)>num.index(b) else 'Bob'if num.index(a)<num.index(b) else'Draw')