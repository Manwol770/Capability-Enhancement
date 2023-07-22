feeling_count = 0

while True :
    o, w = map(int, input().split())

    o_min = o/2
    o_max = o*2

    pet_feeling = ''

    if o == 0 and w == 0 :
        break

    while w > 0 :

        comment, num = map(str, input().split())

        num = int(num)
        if comment == 'E' :
            w -= num
        elif comment == 'F' :
            w += num
        elif comment == '#' :
            if o_max > w > o_min :
                pet_feeling = ':-)'
                feeling_count += 1
            else : 
                pet_feeling = ':-('
                feeling_count += 1
            print(f'{feeling_count} {pet_feeling}')
            break
    
    if w <= 0 :
        while True :

            comment, num = map(str, input().split())

            if comment == '#' :
                pet_feeling = 'RIP'
                feeling_count += 1
                print(f'{feeling_count} {pet_feeling}')
                break