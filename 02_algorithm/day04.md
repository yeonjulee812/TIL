

# 배열

## 2차원 배열

- 1차원 List를 묶어놓은 List
- n X m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법
    
    ```python
    # 행 우선 순회
    for i in range(n): # i 행의 좌표
        for j in range(m): # j 열의 좌표
            Array[i][j] # 필요한 연산 수행
    
    # 열 우선 순회
    for j in range(m):
        for i in range(n):
            Array[i][j] # 필요한 연산 수행
    
    # 지그재그 순회
    # 짝수 번 행에서는 오른쪽 방향, 홀수 번 행에서는 왼쪽 방향으로 순회 
    for i in range(n):
        for j in range(m):
            Array[i][j + (m-1-2*j)*(i%2)] 
            # 필요한 연산 수행
    
    # 델타를 이용한 2차 배열 탐색
    arr = arr[0...N-1][0...N-1]
    # 우하좌상 탐색 시
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    N = 3
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0<=ni<N and 0<=nj<N:
                    print(arr[ni][nj])
    
    N = 3
    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N:
                    print(arr[ni][nj])
    
    # 우하,좌하,좌상,우상 탐색 시
    di = [1, 1, -1, -1]
    dj = [1, -1, -1, 1]
    
    # 한번에 3칸씩 가는 경우 
    N = 3
    P = 3
    for i in range(N):
        for j in range(N):
            for k in range(4):
                for m in range(1, P+1): # p번 붙이기
                    ni = i + di[k] * m
                    nj = j + dj[k] * m
                    if 0<=ni<N and 0<=nj<N:
                        print(arr[ni][nj])
    
    # 전치행렬
    # 인덱스 기준으로 왼쪽 위가 arr[0][0]일 때
    # 대각선(즉, i=j) 기준으로 i < j라면 대각선 우상방 영역에 해당
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(3):
        for j in range(3):
            if i < j: # i > j 도 무관
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
    ```
    
</br>
      
## 부분집합 생성

- 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지를 알아내는 문제
    - 완전검색 기법으로 부분집합 합 문제를 풀기 위해서는, 우선 집합의 모든 부분집합을 생성한 후에 각 부분집합의 합을 계산해야 한다. → 시간 초과 문제
    - 실습
        - 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2**n 개이다.
        - 각 원소가 부분집합에 포함되었는지를 loop를 이용하여 확인하고 부분집합을 생성 및 원소, 원소의 합 출력
            
            ```python
            A = [1, 2, 3, 4]
            bit = [0, 0, 0, 0]
            for i in range(2):
                bit[0] = i                  # 0번째 원소
                for j in range(2):
                    bit[1] = j              # 1번째 원소
                    for k in range(2):
                        bit[2] = k          # 2번째 원소
                        for l in range(2):
                            bit[3] = l      # 3번째 원소
                            print(bit, end = ' ')   #생성된 부분집합 출력
                            for p in range(4):
                                if bit[p]:
                                    print(A[p], end = ' ')  # 부분집합의 원소 출력
                            print()
                            s = 0
                            for p in range(4):
                                if bit[p]:
                                    s += A[p]
                            print(s)    # 부분집합의 원소의 합 출력
            ```
            
    - 보다 간결하게 부분집합을 생성하는 방법
        - 비트 연산자
            - & : 비트 단위로 AND 연산을 한다
            - | : 비트 단위로 OR 연산을 한다
            - << : 피연산자의 비트 열을 왼쪽으로 이동시킨다
            - >> : 피연산자의 비트 열을 오른쪽으로 이동시킨다
        - << 연산자
            - 1 << n: 2^n 즉. 원소가 n개일 경우의 모든 부분집합의 수를 의미한다
        - & 연산자
            - i & (1 <<j) : i의 j번째 비트가 1인지 아닌지를 검사한다
        - 실습
            
            ```python
            arr = [3, 6, 7, 1, 5, 4]
            n = len(arr)    # n : 원소의 개수
            
            for i in range(1<<n):               # 1<<n : 부분집합의 개수
                for j in range(n):              # 원소의 수만큼 비트를 비교함
                    if i & (1<<j):              # i의 j번 비트가 1인 경우
                        print(arr[j], end=", ") # j번 원소 출력
                print()
            print()
            ```
            
        - and과 &의 차이점
            - and는 `논리연산자`로서, 두 개의 조건식이 모두 True일 때 True 리턴되고. 둘 중에 하나라도 False면 False가 리턴됨
            - &는 `비트연산자`로서, 두 개의 이진수에서 동일한 위치의 bit가 1인 것들만 1로 계산
            
            ```python
            and -- 논리연산자
            print(1 and 2) # 2
            print(1 & 2) # 0
            ```
            


## 과목평가 리뷰

- append 함수와 extend 함수의 차이
    - list.append(x)는 리스트 끝에 x 1개를 그대로 넣음
    - list.extend(iterable)는 리스트 끝에 가장 바깥쪽 iterable의 모든 항목을 넣음
    - 실습
        
        ```python
        # 추가하려는 원소가 리스트형
        
        x = ['Tick', 'Tock']
        y = ['Ping', 'Pong']
        x.append(y)
        print('x:', x) # x: ['Tick', 'Tock', ['Ping', 'Pong']]
        
        x.extend(y)
        print('x:', x) # x: ['Tick', 'Tock', ['Ping', 'Pong'], 'Ping', 'Pong']
        
        # 추가하려는 원소가 문자열
        y = 'Ping'
        x.append(y)
        print('x:', x) # x: ['Tick', 'Tock', ['Ping', 'Pong'], 'Ping', 'Pong', 'Ping']
        
        x.extend(y)
        print('x:', x) # x: ['Tick', 'Tock', ['Ping', 'Pong'], 'Ping', 'Pong', 'Ping', 'P', 'i', 'n', 'g']
        ```
        
- 출력예시 헷갈리지 말아야 할 부분
    - 하나라도 0이 있으면 0(False), 둘다 0이 아니면 and 뒤에 위치한 값(True) 반환
        
        ```python
        print(3 and 5) # 5
        print(0 and 5) # 0
        print(5 and 0) # 0
        print(1<<0) # 1 -- 2의 0승
        ```
        
    
- asterisk 다시보기