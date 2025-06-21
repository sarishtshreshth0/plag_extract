def main():
    n = int(input())
    A = list(map(int, input().split()))

    res_list = [0] * 100001

    for num in A:
        res_list[num] += 1
        
        if num != 0:
            res_list[num-1] += 1
        if num != 10**5:
            res_list[num+1] += 1
    
    print(max(res_list))

if __name__ == '__main__':
    main()