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