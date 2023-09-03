import sys
input = sys.stdin.readline

N, M = map(int, input().split())

true_people = list(map(int, input().strip().split()))
true_people_list = [0]*(N+1)
cnt = 0

for i in true_people[1:]:
    true_people_list[i] = 1

start = sum(true_people_list)
end = 0

party_member = [list(map(int, input().strip().split()))[1:] for _ in range(M)]

while start != end:
    start = sum(true_people_list)
    for i in range(M):
        T_F = 0

        for j in party_member[i]:
            if true_people_list[j] == 1:
                T_F = 1
                break
        if T_F:
            for j in party_member[i]:
                true_people_list[j] = 1
    end = sum(true_people_list)

for i in range(M):
    T_F = 0
    for j in party_member[i]:
        if true_people_list[j] == 1:
            T_F = 1
            break
    if not T_F:
        cnt += 1
print(cnt)