num = int(input())

num_list = [float('inf')] * (num + 1)
num_list[0] = 0

for j in range (0,num + 1) :
    i = 1
    while j - i*i >= 0 :
        if  num_list[j] > num_list[j-i*i] + 1 :
            num_list[j] = num_list[j-i*i] + 1

        i += 1

print(num_list[num])