def solution(park, routes):
    delta = { 'E' : (0, 1), 'S' : (1, 0), 'W' : (0, -1), 'N' : (-1, 0)}
    
    W = len(park[0])
    print(W)
    H = len(park)
    print(H)
    
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                x = i
                y = j
    
    for i in routes:
        a, b = i.split()
        b = int(b)
        
        w_x = x
        w_y = y
        for j in range(b):
            
            nx = x + delta[a][0]
            ny = y + delta[a][1]
            
            if 0 <= nx < H and 0 <= ny < W and park[nx][ny] != 'X':
                x = nx
                y = ny
            else:
                x = w_x
                y = w_y
                break   
        
    answer = [x, y]
    return answer