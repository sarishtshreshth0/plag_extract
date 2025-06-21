n = int(input())
inputs = [list(map(int,input().split())) for i in range(n-1)]
out = []
for station_st in range(n-1):
    spend_time = inputs[station_st][1]+inputs[station_st][0] #次の駅に着く時間

    for st_num_cur in range(station_st+1,n-1):
        if spend_time < inputs[st_num_cur][1]:
            spend_time = inputs[st_num_cur][1]

        train_leave_time = inputs[st_num_cur][1] 
        train_i = 0
        wait_time = 0
        if (spend_time%inputs[st_num_cur][2])!=0:
            wait_time = inputs[st_num_cur][2] - (spend_time%inputs[st_num_cur][2])
        spend_time += wait_time + inputs[st_num_cur][0] #次の駅で乗れる電車が出発する時間
        #print("spend",wait_time,spend_time)
    print(spend_time)
print(0)