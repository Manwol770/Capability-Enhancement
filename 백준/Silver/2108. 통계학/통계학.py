import sys
input = sys.stdin.readline

num = int(input())
num_list = []

for i in range (num) :
    num_list.append(int(input()))

arr = sum(num_list)/len(num_list)
print(round(arr))
num_list.sort()
print(num_list[len(num_list)//2])
num_dict = dict(map(lambda x : (x , 0), num_list))

for i in num_list :
    num_dict[i] += 1

new_dict = {}
big_num = max(num_dict.values())

new_dict[big_num] = []

for i in num_dict :
    if num_dict[i] == big_num :
        new_dict[big_num].append(i)

new_dict[big_num].sort()
if len(new_dict[big_num]) > 1 :
    print(new_dict[big_num][1])
else :
    print(new_dict[big_num][0])

print(max(num_list) - min(num_list))