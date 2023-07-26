num = int(input())

cost = []

for j in range (0,num) :
    cost.append(list(map(int, input().split())))

cost.append([0,0,0])
cost = cost[::-1]
cost_dumy_num = [x for x in cost[num]]
cost_dumy_one = [x for x in cost[1]]

case_num_list = []

for a in range (0,3) :
    
    cost[num] = [float('inf'),float('inf'),float('inf')]
    cost[num][a] = cost_dumy_num[a]

    dp = [[float('inf'),float('inf'),float('inf')] for _ in range (num+1)]
    dp[0] = [0,0,0]

    cost[1][a] = float('inf')
    dp[1] = [x for x in cost[1]]
    # cost[1] = [x for x in cost_dumy_one]
    # print(cost)

    for i in range (0,num) :
        for j in range (0,3) :
            for k in range (0,3) :
                if j != k  :
                    dp[i+1][j] = min(dp[i+1][j], cost[i+1][j] + dp[i][k])

    cost[1] = [x for x in cost_dumy_one]
    case_num_list.append(min(dp[num]))

print(min(case_num_list))