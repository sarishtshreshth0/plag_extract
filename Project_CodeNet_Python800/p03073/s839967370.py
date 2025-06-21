#

# import sys
# input=sys.stdin.readline

def main():
    S=input()
    Z1=["1" if i%2==0 else "0" for i in range(len(S))]
    c1=0
    c2=0
    for i in range(len(S)):
        if S[i]!=Z1[i]:
            c1+=1
        else:
            c2+=1
    print(min(c1,c2))
    
if __name__=="__main__":
    main()
