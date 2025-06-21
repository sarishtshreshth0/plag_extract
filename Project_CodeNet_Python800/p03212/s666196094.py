N = None
K = None
cnt = 0 

def rec(num_str):
    global N, K, cnt
    if len(num_str) > K:
        return
    if '7' in list(num_str) and '5' in list(num_str) and '3' in list(num_str):
        if int(num_str) <= N:
           cnt += 1
    rec(num_str+'7') 
    rec(num_str+'5') 
    rec(num_str+'3') 


if __name__ == '__main__':
    S = input()
    N = int(S)
    K = len(S)
    rec('')
    print(cnt)

