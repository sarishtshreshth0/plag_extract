Q, H, S, D = map(int, input().split())
N = int(input())

# Q,H を 1Lあたりの費用に変換する

Q *= 4
H *= 2

one_litter = min(Q, H, S)  # 1L はこれを使う

if 2 * one_litter < D:  # 2Lをサイズのほうが高いときは1Lですべて買う
    ans = N * one_litter
else:  # 偶数を2Lサイズで買い、余りを1Lサイズで買う
    ans = N // 2 * D + (N % 2) * one_litter

print(ans)

