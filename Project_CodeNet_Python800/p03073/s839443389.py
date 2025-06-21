def main():
    s=input()
    a=0  # 0101...
    b=0  # 1010...
    for i, v in enumerate(s):
        if i % 2 == 0:
            if v == "0":
                a+=1
            else:
                b+=1
        else:
            if v == "0":
                b+=1
            else:
                a+=1
    print(min(a,b))

if __name__ == "__main__":
    main()