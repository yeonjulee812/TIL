# 4869. 종이붙이기

T = int(input())

def rec(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return rec(N-10) + rec(N-20)*2

for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}', rec(N))

# 4871. 그래프 경로

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]
    adjM = [[0]*(V+1) for _ in range(V+1)]
    S, G = map(int, input().split())

    for i in range(E):
        v1, v2 = arr[i][0], arr[i][1]
        adjM[v1][v2] = 1  # 유향 그래프

    # print(*adjM, sep='\n')
    stack = [0 for _ in range(V+1)]
    v = S # node
    visited = [0 for _ in range(V+1)] # visited
    top = -1

    while True: # while stack이라고 하면 계속 돌아감(위에서 선언)
        if v == G:
            print(f'#{tc}', 1)
            break
        visited[v] = 1 # 방문
        for w in range(1, V+1):
            if adjM[v][w] and visited[w] == 0: # 인접하고 방문안한 정점 w이 있으면
                top += 1
                stack[top] = v # 정점 v를 stack에 push하고
                v = w # 방문
                break
        else: # 모두 방문했거나 인접한 정점이 없으면 뒤로가기
            if top > -1:
                top -= 1
                v = stack[top+1]
            else:
                print(f'#{tc}', 0)
                break

# 길찾기

for _ in range(10):
    tc, r = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    adjM = [[0]*101 for _ in range(101)] # 분기점 범위: 0~ 99

    for i in range(r):
        v1, v2 = arr[i*2], arr[i*2+1] # v1이 길 시작점
        adjM[v1][v2] = 1 # 유향그래프
    # print(*adjM, sep='\n')

    stack = [0 for _ in range(101)]
    visited = [0 for _ in range(101)]
    top = -1
    v = 0

    while True:
        if v == 99: # 현위치가 도착점이면
            print(f'#{tc}', 1) # 성공
            break
        visited[v] = 1
        for w in range(101):
            if adjM[v][w] and visited[w] == 0: # 길 있는데 간 적없으면
                top += 1
                stack[top] = v # 현위치 기록하고
                v = w # 가
                break
        else: # 길 없거나, 모두 가본 길이면
            if top > -1: # 뒤로 갈 수 있는 상황인지 확인하고 가능하면
                top -= 1
                v = stack[top+1] # 뒤로 가 (pop)
            else: # 더이상 뒤로갈수 없다면 끝
                print(f'#{tc}', 0)
                break

# 미로

def findaway(i, j):
    di = [-1, 0, 0, 1]  # 상좌우하
    dj = [0, -1, 1, 0]
    visited = []
    stack = []

    while True:
        visited.append((i, j))
        v = maze[i][j]
        if v == '3': # 도착했으면
            return 1 # 성공
        else:
            for w in range(4):
                ni, nj = i + di[w], j + dj[w]
                if 0 <= ni <= N-1 and 0 <= nj <= N-1:
                    if maze[ni][nj] != '1' and (ni,nj) not in visited: # 길이 있는데 방문안했으면
                        stack.append((i, j)) # 현재 위치 push하고
                        i, j = ni, nj # 그리로 가
                        break
            else: # 더 이상 갈 곳이 없는 경우
                if stack: # 왔던 길 있으면
                    i, j = stack.pop() # 되돌아가
                else:
                    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    for m in range(N): # 출발점 찾기
        for n in range(N):
            if maze[m][n] == '2':
                i, j = m, n

    print(f'#{tc}', findaway(i, j))


