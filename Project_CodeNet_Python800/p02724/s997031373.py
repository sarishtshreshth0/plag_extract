X=int(input())

def answer(X:int):
    return(int(X/500)*1000+int(X%500/5)*5)

print(answer(X))