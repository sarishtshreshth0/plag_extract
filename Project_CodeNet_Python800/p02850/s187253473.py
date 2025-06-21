from collections import deque
import sys
sys.setrecursionlimit(20000000)

N = int(input())
ab = [list(map(int, input().split())) for _ in range(N-1)]
routes = [[] for _ in range(N)]

for i in range(len(ab)):
    routes[ab[i][0]-1].append([ab[i][1]-1, i])
    routes[ab[i][1]-1].append([ab[i][0]-1, i])

route_color = [-10e+10 for _ in range(len(ab))]

route_num = [0]*N
max_route = 0
for i in range(N):
    num = len(routes[i])
    route_num[i] = num
    if max_route < num:
        max_route = num

seen = [False for _ in range(N)]

def function(num,pre_color):
    color_num = -1
    for route in routes[num]:
        color_num += 1
        if color_num == pre_color:
            color_num+=1
        if route_color[route[1]] != -10e+10:
            color_num-=1
            pass
        else:
            route_color[route[1]] = color_num
            
        if seen[route[0]] == False:
            seen[route[0]] = True
            function(route[0],route_color[route[1]])
    return

function(0,-1)
print(max_route)
for color in route_color:
    print(color+1)