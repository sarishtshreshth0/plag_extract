x = input()
# x = x.replace(1,14)
# replaceは，文字列しか使えない．
ls_x = x.split()

# xに入力した文字列たちを整数化

for i in range(len(ls_x)):
    ls_x[i] = int(ls_x[i])

if ls_x[0] == ls_x[1]:
    print("Draw")

elif ls_x[0] == 1:
    print("Alice")

elif ls_x[1] == 1:
    print("Bob")

elif ls_x[0] > ls_x[1]:
    print("Alice")

elif ls_x[0] < ls_x[1]:
    print("Bob")