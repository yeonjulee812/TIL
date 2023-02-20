
## 큐

- 큐의 특성
    - 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
    - 선입선출구조(FIFO: First In First Out)
    - 주요 연산
        - `enQueue()` : 큐의 뒤쪽(rear)에 원소를 삽입
        - `deQueue()` : 큐의 앞쪽(front)에 원소를 삭제하고 반환
            - front = 마지막으로 디큐된 원소의 인덱스
        - `createQueue()` : 공백상태의 큐를 생성
        - `isEmpty()` : 큐가 공백상태인지를 확인
        - `isFull()` : 큐가 포화상태인지를 확인
        - `Qpeek()` : 큐의 앞쪽에서 원소를 삭제 없이 반환

</br>

- 큐의 구현
    - 초기 공백 큐 생성
        - 크기 n인 1차원 배열 생성
        - front = rear = -1로 초기화
    - 주요 연산
        - 삽입
            - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해 1)rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리 마련, 2)그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장
        - 삭제
            - 가장 앞에 있는 원소를 삭제하기 위해 1)front 값을 하나 증가시켜 큐에 남아있게 될 첫번째 원소 이동, 2)새로운 첫번째 원소를 리턴함으로써 삭제와 동일한 기능
        - 공백상태 및 포화상태 검사
            - 공백상태: front == rear
            - 포화상태: rear == n-1 (n: 배열의 크기, n-1: 배열의 마지막 인덱스)
        - 검색
            - 가장 앞에 있는 원소를 검색하여 반환
            - 현재 front의 한자리 뒤(front+1)에 있는 원소, 즉 큐의 첫 번째에 있는 원소를 반환
    
    </br>

    - 코드
        
        ```python
        queue = [0]*10
        front = rear = -1
        
        # 인큐, 디큐 기본형
        def enqueue(data):
            global rear
            rear += 1 # 새로운 원소 들어갈 자리 마련
            queue[rear] = data # data 저장
        
        def dequeue():
            global front
            front += 1 # 큐에 남아있게 될 첫번째 원소 이동
            return queue[front] # 새로운 첫번째 원소를 리턴해 삭제와 동일한 기능
        
        enqueue(1)
        enqueue(2)
        enqueue(3)
        
        print(dequeue())
        print(dequeue())
        print(dequeue())
        if front != rear: # 에러 안뜨게 안전장치
            print(dequeue())
        if front != rear:
            print(dequeue())
        
        # 함수 선언하지 않아도 무방
        rear += 1 # enqueue(1)
        queue[rear] = 1
        
        # append, pop 사용 - 배열 길어지면 매우 느리게 작동
        q = []
        q.append(10)
        q.append(20)
        q.append(30)
        print(q.pop(0))
        print(q.pop(0))
        print(q.pop(0))
        
        # 덱 활용
        from collections import deque
        q1 = deque()
        q1.append(100)
        q1.append(200)
        q1.append(300)
        print(q1.popleft())
        print(q1.popleft())
        print(q1.popleft())
        ```
        

</br>

- 원형 큐
    - 선형 큐 이용시의 문제점 : 잘못된 포화상태 인식
        - 선형 큐를 이용해 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고 rear = n-1인 상태 즉 포화상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨.
        - 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동시키는 해결방법이 있을 수 있으나, 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐.
        - 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 **원형 형태의 큐**를 이룬다고 가정하고 사용
    
    </br>

    - 구조
        
        ![Untitled](..\img\0220.png)
        
        - 초기 공백상태
            - 크기 n인 1차원 배열 생성
            - front = rear = 0으로 초기화
        - Index의 순환
            - front와 rear의 위치가 배열의 마지막 인덱스인 n-1을 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야 함
            - 이를 위해 나머지 연산자 mod를 사용
        - Front 변수
            - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 **빈자리**로 둠
            - 삽입 위치 및 삭제 위치
                
                ![Untitled](..\img\0220_1.png)
                
        - 공백상태 및 포화상태 검사
            
            ![Untitled](..\img\0220_2.png)
            
        - 삽입
            
            ![Untitled](..\img\0220_3.png)
            
        - 삭제
            
            ![Untitled](..\img\0220_4.png)
            
        - 공백 및 포화상태 검사
            
            ![Untitled](..\img\0220_5.png)