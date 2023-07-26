import sys
input = sys.stdin.readline

num_n = int(input())
num_n_set = set(map(int, input().split()))

num_m = int(input())
num_m_list = list(map(int, input().split()))

for i in num_m_list :
    if i in num_n_set :
        print('1')
    else :
        print('0')