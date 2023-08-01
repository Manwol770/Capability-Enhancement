import sys
input = sys.stdin.readline

N = int(input())
age_name_dict = {}

for i in range (N) :
    age, name = map(str, input().split())
    age = int(age)
    if age not in age_name_dict :
        age_name_dict[age] = [name]
    elif age in age_name_dict :
        age_name_dict[age].append(name)

for i in sorted(age_name_dict) :
    if len(age_name_dict[i]) == 1 :
        print(i, age_name_dict[i][0])
    else :
        for j in range (len(age_name_dict[i])) :
            print(i, age_name_dict[i][j])