import sys

input = sys.stdin.readline

N, K = map(int, input().split())
N = list(map(int, str(N)))
real_N_len = len(N)
N_copy = 0
change = [0] * 21
overlap = [0] * 21
N_set = set()
max_num = 0
min_num = float('inf')
T_F = 0

while len(N) <= 20:
    N = [-1] + N

for i in range(21):
    if N[i] == -1:
        change[i] = 1
    else:
        if N[i] != 9:
            change[i] = 1

N_set.clear()
for i in range(21):
    if N[i] == -1:
        overlap[i] = 0
    else:
        if N[i] not in N_set:
            N_set.add(N[i])
        else:
            overlap[i] = 1

for i in N_set:
    max_num = max(max_num, i)
    min_num = min(min_num, i)

N_len_set = len(N_set)
T_F_set = set()

if K != N_len_set:
    for i in range(20, -1, -1):

        if change[i] == 0:
            continue

        T_F_set.clear()
        for j in range(0, i):
            if N[j] != -1:
                T_F_set.add(N[j])
        T_F_set_len = len(T_F_set)

        max_num = 0
        min_num = float('inf')
        for j in T_F_set:  # 최소 최대
            max_num = max(max_num, j)
            min_num = min(min_num, j)

        if T_F_set_len > K:  # 앞에 있는 수들은 내가 컨트롤 안되니까 K보다 많으면 안됨
            T_F_set.clear()
            continue
        if 21 - i < K - T_F_set_len:
            T_F_set.clear()
            continue
        if T_F_set_len == K:
            if N[i] >= max_num:
                T_F_set.clear()
                continue

        if N[i] == -1:
            if 21 - i < K:
                continue
            N[i] = 1
            T_F_set.clear()
            T_F_set.add(1)
            for j in range(i + 1, 21 - (K - 2)):
                N[j] = 0
                T_F_set.add(0)
            for j in range(21 - (K - 2), 21):
                for k in range(10):
                    if k not in T_F_set:
                        N[j] = k
                        T_F_set.add(k)
                        break
            else:
                break

        N_copy = N[i]  # 여기서 부터 계산식 시작
        if K == T_F_set_len:
            if N[i] == max_num:
                if N[:i + 1].count(N[i]) <= 1:  # 맥스가 이거 하나일때 하나 더해주면 T_F 줄면서 늘어나고
                    N[i] += 1
                else:  # 하나가 아니라면 T_F가 K를 넘어버려서 안됨
                    continue
                for j in range(i + 1, 21):
                    N[j] = min_num
                else:
                    break
            else:  # 최대값 아닐때 돌아감
                for j in range(N[i] + 1, 10):
                    if j in T_F_set:
                        if min_num == N[i]:  # min 값이 이거 하나였으면
                            if N[:i + 1].count(N[i]) <= 1:  # min값 수정
                                min_num = j
                        N[i] = j
                        break
                for j in range(i + 1, 21):
                    N[j] = min_num
                else:
                    break

        elif K > T_F_set_len:

            if 21 - i == K - T_F_set_len:

                for j in range(N[i] + 1, 10):
                    if j not in T_F_set:
                        N[i] = j
                        T_F_set.add(j)
                        break
                else:
                    continue

                for j in range(i + 1, 21):
                    for k in range(10):
                        if k not in T_F_set:
                            N[j] = k
                            T_F_set.add(k)
                            break
                else:
                    break

            N[i] += 1

            T_F_set.clear()
            for j in range(i + 1):  # 집합을 새로 갱신해줌
                if N[j] != -1:
                    T_F_set.add(N[j])
            T_F_set_len = len(T_F_set)

            max_num = 0
            min_num = float('inf')
            for j in T_F_set:  # 최소 최대
                max_num = max(max_num, j)
                min_num = min(min_num, j)

            if K > T_F_set_len:  # 그 집합 개수가 K보다 작을때 계산 뒤에를 0으로 만들어 줄거임
                T_F_set.add(0)
                T_F_set_len = len(T_F_set)
                for j in range(i + 1, 21 - (K - T_F_set_len)):
                    N[j] = 0

                for j in range(21 - (K - T_F_set_len), 21):
                    for k in range(10):
                        if k not in T_F_set:
                            N[j] = k
                            T_F_set.add(k)
                            break
                else:
                    break

            else:  # 104 라인에 집합 개수가 K랑 일치할때 다른 계산법
                for j in range(i + 1, 21):
                    N[j] = min_num
                break

while -1 in N:
    N.remove(-1)
N = list(map(str, N))
print(int(''.join(N)))