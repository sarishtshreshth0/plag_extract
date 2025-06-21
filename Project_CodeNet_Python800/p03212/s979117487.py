import collections
N = int(input())


def generate(n):
    _list = []
    queue = collections.deque([0])
    while queue:
        _temp = queue.popleft()
        if _temp <= n and '3' in str(_temp) and '7' in str(_temp) and '5' in str(_temp):
            _list.append(_temp)
        if len(str(_temp)) > 9:
            break
        queue.append(_temp * 10 + 7)
        queue.append(_temp * 10 + 5)
        queue.append(_temp * 10 + 3)
    return _list


_list = generate(N)
print(len(_list))
