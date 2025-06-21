a,b = map(int,input().split())
s = input()

lst = s.split("-")
#print(lst)
if len(lst[0]) == a and len(lst[1]) == b and len(lst) == 2:
    print("Yes")
else:
    print("No")