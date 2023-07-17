while True :
    num = input()
        
    if num == "0" :
        break

    sentence_num = len(num)

    check_list = []

    for i in range (0,int(sentence_num/2)) :
        if num[i] == num[sentence_num-i-1] :
            check_list.append(1)
        else :
            check_list.append(0)

    if check_list.count(0) == 0 :
        print("yes")
    else :
        print("no")