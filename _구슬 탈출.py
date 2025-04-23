N,M =map(int,input().split())
l = [list("".join(input().split())) for _ in range(N)]

from collections import deque

dx = [1,-1,0,0]
dy = [0,0,-1,1]
cnt = 0
visited = []
def get_position():
    rx, ry, bx,by = 0,0,0,0
    for i in range(N):
        for j in range(M):
            if l[i][j] == "R":
                rx = i
                ry = j
            elif l[i][j] == "B":
                bx = i
                by = j
    return rx,ry,bx,by

def move(x,y,dx,dy):
    cnt = 0
    while l[x+dx][y+dy] !="#" and l[x][y] != "O":
        x+=dx
        y+=dy
        cnt+=1
    return x, y, cnt
def bfs():
    rx, ry, bx, by = get_position()
    q = deque([])
    q.append((rx,ry,bx,by,1))
    visited.append((rx,ry,bx,by))
    while q:
        rx, ry, bx, by,result = q.popleft()
        if result >10:
            result = -1
            break
        for i in range(4):
            nrx,nry,rcnt = move(rx,ry,dx[i],dy[i])
            nbx,nby,ncnt = move(bx,by,dx[i],dy[i])
            if l[nbx][nby] == "O":
                if l[nrx][nry] == "O":
                    result = -1
                    break
                continue
            elif l[nrx][nry] == "O":
                break
            if nrx == nbx and nry == nby:
                if rcnt > ncnt:
                    nrx-=dx[i]
                    nry-=dy[i]
                else:
                    nbx-=dx[i]
                    nby-=dy[i]
            if (nrx,nry,nbx,nby) not in visited:
                visited.append((nrx,nry,nbx,nby))
                q.append((nrx,nry,nbx,nby,result+1))
    return result
print(bfs())