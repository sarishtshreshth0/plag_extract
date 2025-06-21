########関数部分##############
def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X%n)
    return str(X%n)
############################
 
 
#####関数をつかってみる．#####
######今回は二進数に変換######
n, k = map(int, input().split())
x10 = n
x2 = Base_10_to_n(x10, k)
ans = str(x2)
print(len(ans))