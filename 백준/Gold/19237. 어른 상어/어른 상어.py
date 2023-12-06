n,m,k=map(int,input().split())
board=[list(map(int,input().split()))for _ in range(n)] #격자모습
d=list(map(int,input().split())) #상어방향 
shark=[[] for _ in range(m)] #x,y,방향 
rank=[[] for _ in range(m)] #각 상어별 우선순위 


#위-아래-왼쪽-오른쪽
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for i in range(m):
  for _ in range(4): #상어 우선순위 저장 
    rank[i].append(list(map(int,input().split())))

for i in range(n):
  for j in range(n):
    if board[i][j]!=0: #상어 번호: x좌표, y좌표, 방향
        shark[board[i][j]-1]=[i,j,d[board[i][j]-1]-1]
    board[i][j]=[0,0] #격자값 초기화  

#자신의 위치에 냄새 남기기 
def smell(board, shark):
  for i in range(len(shark)):
    if shark[i]: #남아있는 상어에 대하여 
      x,y,d=shark[i] 
      board[x][y]=[k,i] #k시간, 상어번호 저장 
  return board

#1초가 지나면 냄새가 1씩 줄어들기 
def next(board):
  for i in range(n):
    for j in range(n):
      if board[i][j][0]>0: #냄새가 남아있으면 
        board[i][j][0]-=1 #1씩 감소 
  return board

#상어 이동 
def move(shark):
  #임시배열 생성 (겹치는 상어를 제거하기위해)
  temp=[[[]for j in range(n)] for _ in range(n)]
  for i in range(len(shark)): #상어배열을 돌면서 
    if shark[i]: 
      x,y,d=shark[i] 
      candidate=[] #빈자리 
      my_candidate=[] #내냄새가 있는 곳 
      for k in range(4): #상하좌우 
        nx,ny=x+dx[k],y+dy[k]
        if 0<=nx<n and 0<=ny<n: #범위안에있으면 
          if board[nx][ny][0]==0: #빈자리라면 
            candidate.append((nx,ny,k))
          elif board[nx][ny][1]==i: #내냄새가 남아있는곳이라면
            my_candidate.append((nx,ny,k))
      new_d=d #상어의 다음방향 
      if not candidate: #빈자리가 없다면 
        candidate=my_candidate #최종후보군은 내냄새가 남아있는 곳 
      if len(candidate)>=2: #후보군이 여러개라면 
        shark_rank=rank[i][d] #우선순위대로 
        for r in shark_rank:
          flag=False
          for a,b,c in candidate: 
            if r-1==c: #우선순위와 일치하면 
              new_d=r-1 #방향 업데이트 
              flag=True #탈출 
              break
          if flag:
            break
      else: #후보군이 하나라면 
        new_d=candidate[0][2] #바로 방향업데이트 
      shark[i]=[x+dx[new_d],y+dy[new_d],new_d] #상어 최종정보 업데이트
      temp[x+dx[new_d]][y+dy[new_d]].append(i) #임시배열에 저장 

    #임시배열을 돌면서  
    for i in range(n):
      for j in range(n):
        if len(temp[i][j])>1: #상어가 겹치는 칸이있으면 
            temp[i][j].sort() #정렬해서 맨앞 상어만 살리기 
            for k in temp[i][j][1:]:
                shark[k]=[] #나머지 상어는 삭제 

    cnt=0 #남은 상어의 개수 
    for i in range(m):
        if shark[i]!=[]:
            cnt+=1

  return shark,cnt

for i in range(1000):
  board=smell(board,shark) #냄새남기기
  shark,live=move(shark) #상어이동
  board=next(board) #1초 지남 
  if live==1: #1번상어만 남았으면 
    print(i+1) #탈출 
    break
else: #1000초가 지나버린경우 
  print(-1)