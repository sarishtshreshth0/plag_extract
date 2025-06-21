
def main():
    x = int(input())
    sum_m=0
    while x>=500:
        x -= 500
        sum_m+=1000
    while x >=5:
        x -= 5
        sum_m+= 5
    print(sum_m)
if __name__ == "__main__":
    main()