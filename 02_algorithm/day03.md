## APS 기본 및 문제풀이

- 사람의 방법이 아닌, 구현 과정을 중심으로 생각하자!
    - 반복문과 조건문

</br>

- 문제풀이 단계
    - 문제 읽기
    - 접근방법 구상
        - 완전히 새로운 문제는 없다
            - 이전에 풀었던 문제와 유사한지, 특정 자료구조 적용, 전형적인 알고리즘 적용가능한지 체크
        - 문제가 시키는대로 시도
            - 문제 설명대로 예시를 처리하는 것이 접근가능한지 체크(제한조건 내)
            - 여러 입력에 대한 출력을 계산하면서 [규칙성/조건/수식] 적용가능한지 체크
        - 유형/규칙성을 발견하기 힘들다면...
            - 가능한 모든 경우를 처리하면서 풀이가능한지 체크
            - 전체문제가 아닌 일부분으로 나누거나 단계를 나누어 접근
            - 반대로 접근하는 경우를 체크(문제설명, 조건, array 순회 등)
        - 이 모든 접근은 시각적으로(손으로 그리면서)

    - 핵심코드 손코딩
    - 코드구현
    - 디버깅 및 개선

</br>

- 문제풀이 연습
    - 기본기는 철저히 연습
        - 기본기가 탄탄해야 구상한 아이디어를 실수 없이 구현 가능
        - 정확한 입출력, 실수 없는 2차원 array 사용 및 다중 루프제어
        - 가장 효율적인/짧은/멋있는 코드보다 기본적인 [반복/조건]을 빈틈없이 구현
        - 손코딩: 사용하는 주요 array, 범위, 핵심코드를 실명/시각적으로 설계하고 접근
        - 필요한 위치에서 필요한 디버깅 가능하도록 디버거 사용법 익히기
        - 문제읽기 -> 접근방법 구상 -> 핵심코드 손코딩(키보드를 멀리하자!)
    - 나만의 환경/루틴에서 안정적으로 구현
        - 익숙한 환경: 파이참 환경, 폰트, 폰트크기, 창 배치, TC 입력파일, A4용지, 접근순서
        - 익숙한 이름: 입력받는 변수, 선언한 변수, 특정용도 사용 변수 등
        - 익숙한 방법: 함수 호출, 조건, 반복, break, continue 등 익숙한 방법으로 구현

</br>

- 요약
    - 속독: 1~2분 내, 조건/ 제약 체크
    -  TC 손으로 풀기
    - 접근방법 구상: 인간의 방법XXX 나는 CPU다! (제약조건, 범위 고려)
    -  핵심코드 손코딩: 실명제(변수이름) 범위, 익숙한 이름/구조를 써라
    -  코드 구현: 오타 없이 한눈에 보이도록(한 동작)
    -  디버깅 및 개선

</br>

- 예제 : SWEA #6485 (삼성시의 버스노선)

    ```python
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        cnt = [0]*5000

        for _ in range(N): # 지나는 노선 체크
            a, b = map(int,input().split())
            for i in range(a-1, b):
                cnt[i] += 1

        P = int(input())
        num_li = []
        for _ in range(P): # 정류장 리스트화
            num_li.append(cnt[int(input())-1])

        # 노선과 정류장 번호 같으면 프린트
        print(f'#{tc}', *num_li)
    ```