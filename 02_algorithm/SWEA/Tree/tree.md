# 5174. subtree
```python
def pre(T): # 전위순회
    global cnt
    if T:
        cnt += 1
        pre(c1[T])
        pre(c2[T])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split()) # E 간선, N 루트 노드번호
    li = list(map(int, input().split()))
    c1 = [0 for i in range(E+2)] # 먼저나온 자식노드
    c2 = [0 for i in range(E+2)] # 다음에 나온 자식노드

    # 배열에 관계성 저장(부모 인덱스에 자식 번호 저장)
    for i in range(E):
        p, c = li[i*2], li[i*2+1]
        if c1[p] == 0:
            c1[p] = c
        else:
            c2[p] = c

    #자손노드 개수 찾기
    cnt = 0
    pre(N)

    print(f'#{tc} {cnt}')
```

# 1231. 중위순회
```python
def read(i, N): # 중위순회
    global ans
    if i <= N:
        read(i*2, N)
        ans += s[i]
        read(i*2+1, N)

for tc in range(1, 11):
    N = int(input())
    s = [0 for _ in range(N+1)]
    for _ in range(N):
        li = input().split()
        s[int(li[0])] = li[1]
    ans = ''
    read(1, N)
    print(f'#{tc} {ans}')
```


# 5176. 이진탐색

```python
def f(i, N): # 중위순회
    global cnt
    if i <= N: # 딱 떨어지지 않는 경우에는 if문 범위 지정해주면 됨.
        f(i*2, N) # 왼쪽부터 세기 시작해서
        cnt += 1 # 카운트 올려주고(왼쪽 자손의 수만큼 더해준 결과인 cnt에 1 더해줌)
        tree[i] = cnt # 올려준 결과를 트리에 저장
        f(i*2+1, N) # 오른쪽도 세어라(저장된 cnt 활용해서)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    cnt = 0
    f(1,N)
    print(f'#{tc} {tree[1]} {tree[N//2]}')
```