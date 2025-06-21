
def resolve():
    A, B = list(map(int, input().split()))
    if A == B:
        print("Draw")
        return
    if A == 1:
        A = 14
    if B == 1:
        B = 14
    
    if A > B: 
        print("Alice")
    else:
        print("Bob")


if '__main__' == __name__:
    resolve()