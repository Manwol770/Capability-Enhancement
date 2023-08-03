n, k = map(int,input().split())

start_point = k
num_list = [x for x in range (1,n+1)]
print_list = []

for i in range (n) :
    while start_point > len(num_list) :
        start_point -= len(num_list)
    print_list.append(str(num_list[start_point-1]))
    num_list.pop(start_point-1)
    start_point += k - 1

print('<',', '.join(print_list),'>' ,sep="")