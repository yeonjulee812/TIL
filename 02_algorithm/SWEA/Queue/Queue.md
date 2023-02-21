# 5097. 회전
```python
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    front = 0
    for _ in range(M): # dequeue
        front += 1

    print(f'#{tc} {li[front % N]}')
```

```python
# 참고 코드
def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    front += 1
    return queue[front]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split())) + [0]*M
    front = -1
    rear = N-1

    for _ in range(M):
        enqueue(dequeue())
    print(f'#{tc} {dequeue()}')
```

# 5099. 피자 굽기
```python
def enqueue(item):
    global rear
    rear += 1
    queue[rear] = item
 
def dequeue():
    global front
    front += 1
    return queue[front]
 
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    queue = [(0, 0)] * 1000
    front = rear = -1
 
    for i in range(N):  # 최초 인큐
        enqueue((i, C[i]))  # 피자 인덱스, 치즈의 양
 
    last = N - 1  # 화덕에 들어간 피자 번호
    cnt = 0 # 피자 회전 횟수
 
    while True: # while front != rear: 로 비꾸면 두번째 if문 불필요
        cnt += 1
        d = dequeue()
        if d[1] // 2 == 0: # 치즈 다 녹았으면
            if last < M - 1:  # 모든 피자들이 들어갈 때까지
                last += 1
                enqueue((last, C[last]))  # 다음 번호 피자 넣음
 
            if list(map(lambda x: x[1], queue[front:rear])) == [0] * (rear - front):
                break # 화덕에 모든 피자 녹았다면 break
 
        else:
            enqueue((d[0], d[1] // 2))  # 치즈 안녹았으면 동일한 피자 계속 돌림
 
    print(f'#{tc}', queue[cnt - 1][0] + 1)
```

```python
# 참고코드: 선형큐
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
 
    oven = [0]*1000000
    front = -1
    rear = -1
    dough = N            # 오븐에 들어갈 차례인 피자 번호
    door = 0             # 입구로 돌아온 피자 번호
    for i in range(N):      # oven 채우기
        rear += 1
        oven[rear] = i   # 피자번호 - 1 (0번부터, 문제에서는 1번부터)
 
    while front != rear:        # oven이 비어있지 않으면
        front += 1
        door = oven[front]      # 입구로 돌아온 피자를 꺼내고
        pizza[door] //= 2       # 녹은 치즈 기록
        if pizza[door] > 0:     # 치즈가 남아있으면
            rear += 1
            oven[rear] = door   # 다시 투입
        else:                   # 치즈가 모두 녹은 경우
            if dough < M:       # 구울 피자가 남아있으면
                rear += 1
                oven[rear] = dough      # 오븐에 투입
                dough += 1              # 다음에 투입할 피자
    print(f'#{tc} {door+1}')
```

# 5102. 노드의 거리
```python
def bfs(s, g, adj):
    visited = [0]*(V+1)
    queue = []
    queue.append(s) # 출발점 인큐
    visited[s] = 1 # 출발점 인큐표시
    while queue:
        t = queue.pop(0) # 하나 디큐해본 후
        for i in adj[t]: # 방문안한 인접점이 있으면
            if not visited[i]:
                queue.append(i) # 인큐
                visited[i] = visited[t] + 1 # 인큐표시(거리만큼)
    return 0 if visited[g] == 0 else visited[g] - 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split()) # V 노드 개수, E 간선 정보 개수
    adjL = [[] for _ in range(V+1)] # 인접 리스트
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adjL[n1].append(n2)
        adjL[n2].append(n1) # 방향성 없음

    S, G = map(int, input().split()) # S 출발노드, G 도착노드
    print(f'#{tc} {bfs(S, G, adjL)}')

```

# 5105. 미로
```python
di = [-1, 1, 0, 0] # 상하좌우
dj = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)] # 미로
    visited = [[0] * N for _ in range(N)]  # 방문 표시
    queue = [] # 큐 생성
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                queue.append((i, j)) # 출발점 인큐
                visited[i][j] = 1 # 출발점 인큐표시
            elif maze[i][j] == 3:
                si, sj = i, j # 도착점 인덱스 추출
    while queue:
        (i, j) = queue.pop(0) # 디큐
        for dir in range(4):
            ni, nj = i+di[dir], j+dj[dir] # 상하좌우로 인접한 영역 중에서
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1:
                if not visited[ni][nj]: # 길이고 방문안한 정점이 있으면
                    queue.append((ni, nj)) # 인큐
                    visited[ni][nj] = visited[i][j] + 1 # 방문 표시

    ans = visited[si][sj]-2 if visited[si][sj]>=1 else 0 # 경로 없으면 0 주의
    print(f'#{tc} {ans}')
```

```python
# 참고 코드(BFS 기본형)
def bfs(i, j, N):
    visited = [[0]*N for _ in range(N)] # 인큐 확인배열
    q = [(i,j)]             # 큐 생성, 시작점 인큐
    visited[i][j] = 1       # 시작점 표시
    while q:                # 큐가 비어있지 않으면
        i, j = q.pop(0)
        if maze[i][j]=='3': # i,j가 도착지인가?
            return visited[i][j] - 2
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!='1' and visited[ni][nj]==0: # 벽이 아니고, 인큐한 적 없으면
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0        # '3'칸에 못가는 경우
 
def findStart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j]=='2':
                return i, j
    return -1, -1       # return 형식 맞추기용
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
 
    # si = sj = -1
    # for i in range(N):
    #     for j in range(N):
    #         if maze[i][j]=='2':
    #             si, sj = i, j
    #             break
    #     if si!=-1:
    #         break
    si, sj = findStart(N)
 
    print(f'#{tc} {bfs(si, sj, N)}')
```