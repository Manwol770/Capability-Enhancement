num = int(input())

people_list = []

for i in range (num) :
    people_list.append(tuple(map(int,input().split())))
    people_dict = dict(list(map(lambda x : (x , 0) , people_list)))

count = 0

for i in people_list :
    count = 1
    for j in people_list :
        if j[0] > i[0] and j[1] > i[1] :
            count += 1
    people_dict[i] = count

for i in people_list :
    print(people_dict[i], end= ' ')