N = int(input())
w = [input() for i in range(N)]


if len(set(w)) == N: #set:重複なしのリスト(型はlistではなく、set)
    if all(w[i][-1] == w[i+1][0] for i in range(N-1)):
        print("Yes")
        exit() #プログラムを終了

print("No")