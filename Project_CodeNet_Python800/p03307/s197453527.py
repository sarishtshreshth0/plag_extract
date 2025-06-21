from fractions import gcd

def main():
    def lcm(a,b):
        return a*b//gcd(a,b)

    print(lcm(2,int(input())))

if __name__ == '__main__':
    main()