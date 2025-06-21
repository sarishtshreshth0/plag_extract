N, K = map(int, input().split())

def conv(N, K):
    if (int(N/K)):
        return conv(int(N/K), K)+str(N%K)
    return str(N%K)

print(len(conv(N, K)))