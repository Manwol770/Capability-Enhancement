num = int(input())

five_count = 0

for i in range (1,num+1) :
    while i % 5 == 0 :
        five_count += 1
        i /= 5

zero_count = five_count

print(zero_count)