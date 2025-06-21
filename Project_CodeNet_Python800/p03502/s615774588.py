n=int(input())
def sum_of_digit(n):
    res=0
    while n>0:
        res+=n%10
        n=n//10
    return res
print('Yes' if n % sum_of_digit(n)==0 else 'No')