#入力
lst = input().split()

A = int(lst[0])
B = int(lst[1])

#判定
if A == 1 or B == 1:
   if A == B == 1:
      result = 'Draw'
   elif A == 1:
      result = 'Alice'
   elif B == 1:
      result = 'Bob'
else:
   if A == B:
      result = 'Draw'
   elif A < B:
      result = 'Bob'
   elif A > B:
      result = 'Alice'

#出力
print(result)