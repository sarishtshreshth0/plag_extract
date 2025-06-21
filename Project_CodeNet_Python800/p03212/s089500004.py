def cal(N,n_str):
    n_list = ["7","5","3"]

    if len(n_str) != 0:
        if int(n_str) <= N:
            if len(n_str) == len(str(N)) and len(set(list(n_str))) == 3:
                return 1
            elif len(n_str) == len(str(N)) and len(set(list(n_str))) < 3:
                return 0
            elif len(n_str) < len(str(N)) and len(set(list(n_str))) == 3:
                return 1 + cal(N,n_str+"7") + cal(N,n_str+"5") + cal(N,n_str+"3")
            elif len(n_str) < len(str(N)) and len(set(list(n_str))) < 3:
                return cal(N,n_str+"7") + cal(N,n_str+"5") + cal(N,n_str+"3")
        else:
            return 0
    else:
        return cal(N,n_str+"7") + cal(N,n_str+"5") + cal(N,n_str+"3")

def main():
    N = int(input())

    print(cal(N,""))

if __name__ == "__main__":
    main()
