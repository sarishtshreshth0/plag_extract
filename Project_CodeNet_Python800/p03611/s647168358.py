def solve():
    
    N = int(input())
    a  = list(map(int, input().split()))

    lists = [0] * ((10**5)+2)

    for i in a:
        lists[i] += 1
        lists[i+1] += 1
        lists[i-1] += 1

    print(max(lists))    

if __name__ == "__main__":
    solve()
