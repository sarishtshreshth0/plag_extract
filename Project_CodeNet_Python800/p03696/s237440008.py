from sys import stdin
def main():
    #入力
    readline=stdin.readline
    n=int(readline())
    s=readline().strip()

    left_left=0
    need_left=0
    for i in range(n):
        if s[i]=="(":
            left_left+=1
        else:
            if left_left>0:
                left_left-=1
            else:
                need_left+=1

    print("("*need_left+s+")"*left_left)

if __name__=="__main__":
    main()