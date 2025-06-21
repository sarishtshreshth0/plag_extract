def get_section_arr(X):
    return [(X[i+1]-X[i]) for i in range(len(X)-1) ]
if __name__ == "__main__":
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    X.sort()
    section_arr = get_section_arr(X)
    section_arr.sort(reverse=True)
    print((X[-1]-X[0]) - (sum(section_arr[:N-1])))
