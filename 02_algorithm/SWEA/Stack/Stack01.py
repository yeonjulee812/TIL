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