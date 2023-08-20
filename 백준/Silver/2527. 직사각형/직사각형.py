for tc in range (4) :
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())

    result = 'd'
    cnt = 0
    x = 0
    y = 0

    for i in range (x2,p2+1) :
        for j in range (y2,q2+1) :
            if x1 <= i <= p1 and y1 <= j <= q1 :
                cnt += 1
                if cnt == 1:
                    result = 'c'
                elif cnt > 1 and result == 'c':
                    result = 'b'
                    x = i
                    y = j
                    break
                if i != x and j != y and result == 'b':
                    result = 'a'
                    break
        if result == 'a' :
            break
    print(result)