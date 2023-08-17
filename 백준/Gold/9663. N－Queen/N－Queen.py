import sys
input = sys.stdin.readline

def N_Queen(N, x_visited, y_visited) :           # 재귀 돌려줄 함수 (N은 x축을 담당할 것임)
    global cnt                      # cnt 에는 체스판 완성 횟수를 의미한다.
    global cnt2

    if N == Num :                   # 재귀의 끝점까지 도달하면
                                    # = 체스판 끝까지 퀸을 놓았다면
        cnt += 1                    # 체스판 완성을 의미함으로 cnt 를 1개 늘려주고
        return                      # 뒤로 돌아감

    for i in range (Num) :          # 체스판을 y축을 계속 가줄 for문
        T_F = 1
        if y_visited[i] == 0 :
            for j in range (0, -Num-1, -1) :
                nx_1 = N+j
                ny_1 = i+j
                if 0 <= nx_1 < Num and 0 <= ny_1 < Num :
                    if matrix[nx_1][ny_1] :
                        T_F = 0
                        break
                else :
                    break
            for j in range (0, -Num-1, -1) :
                nx_2 = N-j
                ny_2 = i+j
                if 0 <= nx_2 < Num and 0 <= ny_2 < Num :
                    if matrix[nx_2][ny_2] :
                        T_F = 0
                        break
                else :
                    break
            for j in range (0, Num) :
                nx_2 = N-j
                ny_2 = i+j
                if 0 <= nx_2 < Num and 0 <= ny_2 < Num :
                    if matrix[nx_2][ny_2] :
                        T_F = 0
                        break
                else :
                    break
            for j in range (0, Num) :
                nx_2 = N+j
                ny_2 = i+j
                if 0 <= nx_2 < Num and 0 <= ny_2 < Num :
                    if matrix[nx_2][ny_2] :
                        T_F = 0
                        break
                else :
                    break
            if T_F :
                x_visited[N] = 1
                y_visited[i] = 1
                matrix[N][i] = 1
                N_Queen(N+1, x_visited, y_visited) # 재귀를 돌린다 (이 x축에 퀸을 놓았으니 x 축을 한칸더 가서 Y축을 다시 보겠다는 의미)
                x_visited[N] = 0
                y_visited[i] = 0
                matrix[N][i] = 0
    return                              # for문을 다 돌았는데도 체스를 못놓았다면 다음으로 갈 필요없이 다시 위(x-1)로 돌아감


Num = int(input())                # 받아오는 N

cnt = 0
cnt2 = 0
y_visited = [0]*Num
x_visited = [0]*Num
matrix = [[0]*Num for _ in range (Num)]

N_Queen(0, x_visited, y_visited)
print(cnt)