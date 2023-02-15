# 4866. 괄호검사

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

# 4873. 반복문자 지우기

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

# 2005. 파스칼의 삼각형

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

# 1234. 비밀번호

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

# 1217. 거듭제곱

def sq(b, e):
    if e == 1:
        return b
    else:
        return b*sq(b, e-1)

for _ in range(1, 11):
    tc = int(input())
    b, e = map(int, input().split())

    print(f'#{tc}', sq(b, e))

# Forth

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

# 계산기1

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
