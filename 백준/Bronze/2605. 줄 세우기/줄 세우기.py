import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int ,input().split()))
people_list =[]
num = 1

for n in N_list :
    people_list = people_list[0:len(people_list)-n] + [num] + people_list[len(people_list)-n : len(people_list)]
    num += 1

print(*people_list)