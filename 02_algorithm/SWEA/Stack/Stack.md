# 4866. 괄호검사
```
T = int(input())

open_li = ['(', '{', '[']
close_li = [')', '}', ']']

for tc in range(1, T+1):
    s = input()
    stack = [0] * 100
    top = -1
    ans = 1

    for x in s:
        if x in open_li: # 여는 괄호 있으면 push
            top += 1
            stack[top] = x
        elif x in close_li: # 닫는 괄호 있으면
            if top > -1 and open_li.index(stack[top]) == close_li.index(x): # 스택에 여는 괄호 있고 괄호 형태도 같으면 pop
                top -= 1
            else: # 스택에 여는 괄호 없거나, 괄호 형태 다르면
                ans = 0 # 오류
                break
    else: # 문자열 검토 끝
        if top > -1: # 스택에 여는 괄호 남아있으면
            ans = 0 # 오류

    print(f'#{tc}', ans)
```

# 4873. 반복문자 지우기
```
T = int(input())
for tc in range(1, T+1):
    s = input()
    stack = [0] * 1000
    top = -1
    ans = 1

    for x in s:
        if x == stack[top]: # 연속문자이면 pop
            top -= 1
        else: # 연속문자 아니면 push
            top += 1
            stack[top] = x

    print(f'#{tc}', top + 1)
```

# 2005. 파스칼의 삼각형
```
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = [[1]*num for num in range(1, 11)]

    for i in range(N):
        if i > 1:
            for x in range(1, i):
                ans[i][x] = ans[i-1][x-1] + ans[i-1][x]

    print(f'#{tc}')
    for row in ans[:N]:
        print(*row)
```

# 1234. 비밀번호
```
for tc in range(1, 11):
    l, s = map(str, input().split())
    stack = [0] * 100
    top = -1
    ans = 1

    for x in s:
        if x == stack[top]: # 연속문자이면 pop
            top -= 1
        else: # 연속문자 아니면 push
            top += 1
            stack[top] = x

    print(f'#{tc}', ''.join(stack[:top+1]))
```

# 1217. 거듭제곱
```
def sq(b, e):
    if e == 1:
        return b
    else:
        return b*sq(b, e-1)

for _ in range(1, 11):
    tc = int(input())
    b, e = map(int, input().split())

    print(f'#{tc}', sq(b, e))
```

# Forth
```
T = int(input())
for tc in range(1, T+1):
    li = input().split()
    stack = []

    for i in li:
        if i == '.': # 코드 종료
            if len(stack) > 1: # . 이후에도 스택에 두 개 이상의 피연산자가 남아있으면 에러
                result = 'error'
            else: # 정상종료
                result = stack.pop()
            break
        elif i.isdigit(): # 숫자이면
            stack.append(int(i))
        else: # 연산자이면
            if len(stack) > 1: # 연산가능한 경우
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '*':
                  stack.append(a*b)
                elif i == '/':
                    stack.append(int(a/b))
            else: # 연산불가능한 경우
                result = 'error'
                break

    print(f'#{tc}', result)
```

# 계산기1
```
for tc in range(1, 11):
    N = int(input())
    li = list(input())
    stack = []
    postfix = ''

    # 후위표기식으로 변환
    for i in li:
        if i.isdigit(): # 숫자이면
            postfix += i # 출력
        else: # + 연산자가 나오면
            if not stack: # 스택이 비어있으면
                stack.append(i)
            else:
                postfix += stack.pop() # 스택 안에 있는 거 꺼내고
                stack.append(i) # 스택에 넣기

    while stack: # 스택에 연산자가 남아있으면
        postfix += stack.pop() # 꺼내기

    # 후위표기식을 계산
    calc_stack = []
    for i in postfix:
        if i.isdigit():
            calc_stack.append(int(i))
        else:
            b = calc_stack.pop()
            a = calc_stack.pop()
            calc_stack.append(a+b)

    print(f'#{tc}', calc_stack.pop())
```

# 4881. 배열 최소합
```
def f(i, k):
    global minsum
    if i == k:
        sum = 0
        for col, row in enumerate(p):
            sum += li[row][col]
        if minsum > sum:
            minsum = sum
            return minsum
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i] # 자리바꾸기
            f(i+1, k) # 결정된 자리 다음부터의 경우의 수
            p[i], p[j] = p[j], p[i] # 원상복구
```
```
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    p = [i for i in range(N)]
    minsum = 90
    f(0, N)
    print(f'#{tc}', minsum)
```

# 4880. 토너먼트 카드게임
```
def game(i, j): # 한 팀씩 뽑아주자
    if i == j:
        return i
    else:
        m = (i+j)//2
        r1 = game(i, m)
        r2 = game(m+1, j)
        return winner(r1,r2)

def winner(a, b): # 둘이서 가위바위보
    A, B = cards[a-1], cards[b-1]
    pair = {(1, 2):2, (2, 3):3, (3, 1):1}
    if A == B:
        return a # 비기면 작은 번호가 승자
    for p, v in pair.items():
        if (A, B) == p:
            return b if p.index(v) else a
        elif (B, A) == p:
            return a if p.index(v) else b
```
```
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    print(f'#{tc}', game(1,N))
```

# 계산기 2
```
for tc in range(1, 11):
    N = int(input())
    li = list(input())
    stack = [0] * N
    top = -1
    postfix = ''
    op = {'*':2, '+':1}

    # 후위표기식으로 변환
    for i in li:
        if i.isdigit(): # 연산자가 아니면
            postfix += i
        else: # 연산자
            if top == -1 or op[stack[top]] < op[i]: # 스택이 비어있거나 우선순위 높은 연산자를 만나면
                top += 1
                stack[top] = i # push
            else:
                while top > -1 and op[stack[top]] >= op[i]: # 스택에 남아있고 남아있는 연산자가 우선순위가 같거나 낮은 경우동안
                    top -= 1
                    postfix += stack[top+1] # 연산자를 pop
                top += 1
                stack[top] = i # 현재 (우선순위 높은) 연산자를 push

    while top > -1: # 연산자가 남아있으면
        top -= 1
        postfix += stack[top+1] # 남아있는 연산자 들어간 순서대로 모조리 pop

    # 후위표기식 계산
    calc_stack = [0]*N
    top = -1

    for i in postfix:
        if i.isdigit(): # 피연산자를 만나면
            top += 1
            calc_stack[top] = int(i) # push
        else:
            top -= 1
            b = calc_stack[top+1]
            top -= 1
            a = calc_stack[top+1]

            if i == '*':
                top += 1
                calc_stack[top] = a*b
            elif i == '/':
                top += 1
                calc_stack[top] = int(a/b)
            elif i == '+':
                top += 1
                calc_stack[top] = a+b
            elif i == '-':
                top += 1
                calc_stack[top] = a-b

    print(f'#{tc}', calc_stack[top])
```

