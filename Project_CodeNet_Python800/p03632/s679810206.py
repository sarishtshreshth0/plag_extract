
a, b, c, d = map(int, input().strip().split())


def func(a_sec, b_sec, c_sec, d_sec):
    if a_sec < c_sec <= b_sec < d_sec:
        temp = b_sec - c_sec
    elif c_sec < a_sec <= d_sec < b_sec:
        temp = d_sec - a_sec
    elif a_sec <= c_sec < d_sec <= b_sec:
        temp = d_sec - c_sec
    elif c_sec <= a_sec < b_sec <= d_sec:
        temp = b_sec - a_sec
    else:
        temp = 0

    print(temp)


func(a_sec=a, b_sec=b, c_sec=c, d_sec=d)
