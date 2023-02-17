# 10760. 우주선착륙2
```
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 테두리를 0으로 패딩
    li = [[0]*(M+2) for _ in range(N+2)]
    mars = [list(map(int, input().split())) for _ in range(N)]
    for si in range(N):
        for sj in range(M):
            li[si+1][sj+1] = mars[si][sj]

    # 예비후보지 찾기
    candidate = 0
    for si in range(1, N+1):
        for sj in range(1, M+1):
            cnt = 0
            for di, dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
                if 0< li[si+di][sj+dj] < li[si][sj]:
                    cnt += 1
            if cnt >=4: # 4방향 이상에서 사진찍을 수 있으면
                candidate += 1 # 예비후보지에 해당

    print(f'#{tc} {candidate}')
```

# 9489. 고대유적
```
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]

    h_max = v_max = 0
    for i in range(N):
        h_cnt = 0 # 가로 형태 구조물의 최대 길이
        for j in range(M):
            if li[i][j] == 1:
                h_cnt += 1
            else:
                h_cnt = 0
            if h_max < h_cnt:
                h_max = h_cnt

    for j in range(M):
        v_cnt = 0 # 세로 형태 구조물의 최대 길이
        for i in range(N):
            if li[i][j] == 1:
                v_cnt += 1
            else:
                v_cnt = 0
            if v_max < v_cnt:
                v_max = v_cnt

    maxV = h_max # 최대 길이
    if maxV < v_max:
        maxV = v_max

    print(f'#{tc} {maxV}')
```

```
# 강사님 코드 참고
# import sys
# sys.stdin = open("input_01.txt", "r")

def count(arr):
    mx = 2
    for lst in arr:
        cnt = 0
        for n in lst:
            if n==1:
                cnt += 1
                if mx < cnt:
                    mx = cnt
    return mx


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_t = list(map(list, zip(*arr)))

    ans = count(arr)
    t = count(arr_t)
    if ans < t:
        ans = t
    print(f'#{tc} {ans}')
```

# 5432. 쇠막대기 자르기
```
T = int(input())
for tc in range(1, T+1):
    s = input()
    cnt = cum = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if s[i-1] == '(': # 레이저
                cum += cnt
            else: # 막대기의 끝
                cum += 1

    print(f'#{tc} {cum}')
```

# 4615. 재미있는 오셀로 게임
```
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N+2) for _ in range(N+2)] # 테두리를 0으로 패딩

    n = N//2
    arr[n][n+1] = arr[n+1][n] = 1 # 흑돌 초기상태
    arr[n][n] = arr[n+1][n+1] = 2 # 백돌 초기상태
    bcnt = wcnt = 0

    for _ in range(M):
        i, j, c = map(int, input().split())
        arr[i][j] = c

        for di, dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
            li = [] # 색깔 바꿀 돌들의 위치
            for mul in range(1, N):
                ni, nj = i+di*mul, j+dj*mul
                if arr[ni][nj] == 0: # 칸이 비어있거나 테두리에 다다랐을 때
                    break
                elif arr[ni][nj] != c: # 다른 색깔 돌 있을 때
                    li.append((ni, nj))
                else: # 같은 색깔 돌 있을 때
                    while li:
                        ti, tj = li.pop()
                        arr[ti][tj] = c # 색깔 바꿔
                    break

    for i in range(1,N+1):
        for j in range(1,N+1):
            if arr[i][j] == 1:
                bcnt += 1
            elif arr[i][j] == 2:
                wcnt += 1

    print(f'#{tc} {bcnt} {wcnt}')
                # 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력
```

# 4408. 자기 방으로 돌아가기
```
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [0 for i in range(200)]

    for _ in range(N):
        s, e = map(lambda x: (int(x)-1)//2, input().split()) # 현재 방위치(s)와 돌아가야 할 방의 위치(e)를 복도 번호로 바로 변환
        if s>e:
            s, e = e, s
        for i in range(s,e+1):
            arr[i-1] += 1

    maxV = 0
    for v in arr:
        if maxV < v:
            maxV = v

    print(f'#{tc} {maxV}')
```

# 1859. 백만장자 프로젝트
```
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))

    maxP = s = 0
    for i in range(len(price)-1,-1,-1):
        if maxP < price[i]:
            maxP = price[i] # 최고가
        s += maxP - price[i]

    print(f'#{tc} {s}')
```

```
# 강사님 코드 참고
# 풀이 1 - O(n^2)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))

    i = ans = 0
    while i < N:
        # [1] i ~ 끝까지 최댓값의 index 찾기
        i_mx = i
        for j in range(i+1, N):
            if li[i_mx] < li[j]:
                i_mx = j

        # [2] i ~ i_mx 까지의 최대값과의 차이 누적
        for j in range(i, i_mx):
            ans += li[i_mx] - li[j]

        i = i_mx + 1

    print(f'#{tc} {ans}')

# 풀이 2 - 뒤쪽부터 체크하는 방법(DP) O(n)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))[::-1]

    ans = mx = 0
    for n in li:
        if mx>n:
            ans += mx - n
        else:
            mx=n
```