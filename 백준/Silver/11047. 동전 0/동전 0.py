import sys
input = sys.stdin.readline

N,K=map(int,input().split())
num_list=[]
count = 0

for i in range(N):
    num_list.append(int(input()))

for j in range((N-1),-1,-1):
    if(K>=num_list[j]):
        count += K//num_list[j]        
        K -= (K//num_list[j] * num_list[j])

print(count)