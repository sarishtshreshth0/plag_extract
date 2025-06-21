a,b = map(int,(input().split()))
def yn(p):
    if p:
        return "Yes"
    else:
        return "No"
print(yn(a*b%2==1))