def main():
    n = int(input())
    m = 1
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            m = i
    m_ = n//m
    print(max(len(str(m_)),len(str(m))))

if __name__ == "__main__":
    main()
