N = int(input())

# lst = list(map(int, input().split()))
lst = list(map(int, input().split()))

new_set = set()

if 1 in lst :
    N -= 1

for _ in range (0, len(lst)) :

    list_num = lst.pop()
    for j in range (2,list_num) :
        if list_num % j == 0 :
            new_set.add(list_num)
            break

print(N-len(new_set))