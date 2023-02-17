# 4835. 구간합
```
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    maxV = 0
    minV = 1000000

    for i in range(N-M+1):  # 더하려는 범위의 왼쪽 끝
        s = 0               # 구간합
        for j in range(i, i+M):
            s += arr[j]

        if maxV < s:
            maxV = s
        if minV > s:
            minV = s

    print(f'#{tc} {maxV-minV}')
```

# 4828. min max
```
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    maxV = arr[0]
    minV = arr[0]

    for i in range(N):
        if maxV < arr[i]:
            maxV = arr[i]
        if minV > arr[i]:
            minV = arr[i]

    print(f'#{tc} {maxV-minV}')
```

# 10548. Gravity
```
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    diff = [0]*N    # 낙차 구하기
    for i in range(N):
        diff[i] += N - i - 1
        for j in range(i+1, N):
            if arr[i] <= arr[j]:
                diff[i] -= 1

    maxV = 0    # 낙차 최댓값 구하기
    for i in range(N):
        if maxV < diff[i]:
            maxV = diff[i]

    print(f'#{tc} {maxV}')
```

# 1966. 숫자를 정렬하자
```
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f'#{tc}', *arr)
```

# 1206. View
```
for tc in range(1, 11):
	N = int(input())
	arr = list(map(int, input().split()))
	view = 0

	for i in range(2, N -2): # 구간의 왼쪽 끝
		maxV = 0
	
		for j in range(i-2, i+3):
			if maxV < arr[j] and i != j:
				maxV = arr[j] # 구간 내 최댓값
			
		if maxV < arr[i]:
			view += arr[i] - maxV

	print(f'#{tc}', view)

```

# 4834. 숫자 카드
```
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    cnt = [0]*11
    for i in arr:
        cnt[i] += 1
    idx, max_num = 0, 0
    for i in range(11):
        if idx <= cnt[i]:
            idx = cnt[i]
            max_num = i

    print(f'#{tc}', max_num, idx)
```

# 4831. 전기버스
```
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    li = list(map(int, input().split()))

    busstop = [0]*(N+1)
    for i in li:    # 충전기가 설치된 정류장 리스트
        busstop[i] = 1

    last = 0    # 마지막 충전위치
    next = K     # 충전 후 최대로 갈 수 있는 정류장 번호
    cnt = 0

    while (next < N):
        if busstop[next]:
            last = next
            next = last + K
            cnt += 1
        else:
            tmp = 0
            for i in range(last+1, next):
                if busstop[i]:
                    tmp = i
            if tmp != 0:
                last = tmp
                next = last + K
                cnt += 1
            else:
                cnt = 0
                break
    print(f'#{tc}', cnt)
```

# 1208. Flatten
```
for tc in range(1,11):
    D = int(input())
    li = list(map(int, input().split()))

    maxV, minV = 50, 50
    for i in range(100):
        if maxV < li[i]:
            maxV = li[i]
        if minV > li[i]:
            minV = li[i]

    cnt = 0
    diff = maxV - minV

    while diff >= 2:
        li[li.index(maxV)] -= 1
        li[li.index(minV)] += 1
        cnt += 1
        maxV, minV = 0, 100
        for i in range(100):
            if maxV < li[i]:
                maxV = li[i]
            if minV > li[i]:
                minV = li[i]
        diff = maxV - minV

        if cnt == D:
            break

    print(f'#{tc}', diff)
```

# 9386. 연속한 1의 개수
```
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = input()

    maxV = 0
    for i in li.strip('0').split('0'):
        if maxV < len(i):
            maxV = len(i)

    print(f'#{tc}', maxV)
```

