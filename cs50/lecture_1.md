
# C 기초

```c
#include <stdio.h> -- stdio.h 라는 이름의 파일을 찾아 printf 함수에 접근할 수 있게 

int main(void) # 시작
{
    printf("hello, world\n");
}
```
</br>

## 컴파일러

- 우리가 직접 작성한 코드는 ‘소스 코드’라 하며, 이를 2진수로 작성된 ‘머신 코드’로 변환해야 컴퓨터가 이해할 수 있음. 이러한 작업을 컴파일러라는 프로그램이 수행해줌.

![cs50_1.png](../img/cs50_1.png)

```c
[Terminal]

$ clang hello.c -- clang이라는 컴파일러로 hello.c라는 소스코드를 컴파일해라
$ ./a.out -- 현재 디렉토리에 있는 a.out이라는 프로그램을 실행해라
# hello, world

$ clang hello.c
$ ./hello
# hello, world

```

```c
string answer = get_string("What's your name?\n");
printf("hello, %s\n", answer);
```

- 변수(answer)가 저장하는 데이터의 종류를 정확히 명시해야 하며, 이때 문자열을 의미하는 string과 같은 형식지정자를 앞에 입력해줌.
- =는 할당 연산자로서, 오른쪽에 있는 값을 왼쪽에 지정한다는 의미. 즉, get_string 함수가 사용자의 이름을 반환하면 그 이름을 answer이라는 변수에 저장. 이때 컴퓨터의 메모리 어딘가에 사용자의 이름이 저장되는 것.
- 이름이라는 ‘문자열’을 받기 때문에 string에서의 s를 % 뒤에 붙여 인자를 받아줌

```c
[Terminal]
$ clang -o string string.c -lcs50
# -o string은 string.c를 string.out이라는 머신코드로 저장하도록 하는 명령어
# -lcs50은 'link cs50' 즉 컴파일 시 cs50 파일을 연결하라는 의미

# 위의 복잡한 과정 대신에, make 명령어로써 간단히 컴파일 가
make hello
make string
```

- make hello : hello.c라는 파일(소스코드)을 찾고, 찾고 나면 hello라는 파일(머신코드)을 만듦
- make는 리눅스라는 운영체제에 있는 프로그램으로 요즘은 맥과 윈도우에도 포함되어 있음(CS50 샌드박스라는 클라우드 기반 환경에 저장되어 있음)

</br>

## 조건문과 루프

- 조건문 예시

```c
int counter = 0;
counter ++;

if (x < y)
{
	printf("x is less than y\n");
}

if (x < y)ㄷ
{
	printf("x is less than y\n");
}
else
{
	printf("x is not less than y\n");
}

if (x < y)
{
	printf("x is less than y\n");
}
else if (x > y)
{
	printf("x is greater than y\n");
}
else if (x == y) # 일치 연산자
{
	printf("x is equal to y\n"); 
}
```

- 루프

```c
while (true)
{
	printf("hello, world\n");
}

int counter = 0;
int i = 0;
while (i < 50)
{
	printf("hello, world\n");
	i++;
}

for (int i = 0; i < 50; i++)
{
	printf("hello, world\n");
}
```

</br>

## 자료형, 형식 지정자, 연산자

- get_int, get_string과 같은 cs50 라이브러리 내 함수들은 사용자로 하여금 특정한 자료형의 값을 입력하도록 강제(에러 방지 위함)
    - 해당 자료형이 입력될 때까지 같은 질문을 반복
    - 오류 검증 작업을 신경쓰지 않아도 되고 원하는 기능을 구현하는 데 집중할 수 있음
- int
    
    ```c
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        int age = get_int("What's your age?\n");
        printf("You are at least %i days old.\n", age * 365);
    }
    ```
    
- float
    
    ```c
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        float price = get_float("What's the price?\n");
        printf("Your total is %.2f.\n", price * 1.0625);
    }
    ```
    
- parity(홀짝 검증)
    
    ```c
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        int n = get_int("n: ");
    
        if (n % 2 == 0)
        {
            printf("even\n");
        }
    
        else
        {
            printf("odd\n");
        }
    }
    ```
    
- [참고] 주석의 활용
    
    ```c
    // Conditions and relational operators
    
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        // Prompt user for x
        int x = get_int("x: ");
    
        // Prompt user for y
        int y = get_int("y: ");
    
        // Compare x and y
        if (x < y)
        {
            printf("x is less than y\n");
        }
        else if (x > y)
        {
            printf("x is greater than y\n");
        }
        else
        {
            printf("x is equal to y\n");
        }
    }
    ```
    
</br>

## 사용자 정의 함수, 중첩 루프

- 반복 출력의 다양한 예시
    
    ```c
    # 1. 단순 반복 -- 피해야 할 방법
    #include <stdio.h>
    
    int main(void)
    {
        printf("cough\n");
        printf("cough\n");
        printf("cough\n");    
    }
    
    # 2. for loop
    #include <stdio.h>
    
    int main(void)
    {
        for (int i = 0; i < 3; i++)
        {
            printf("cough\n");
        }
    }
    
    # 3. 사용자 정의 함수
    #include <stdio.h>
    
    void cough(void)
    {
        printf("cough\n");
    }
    
    int main(void)
    {
        for (int i = 0; i < 3; i++)
        {
            cough(); -- 추상화
        }
    ```
    
- main 함수를 위로 올리고 cough 함수를 내려봅시다.
    
    ```c
    #include <stdio.h>
    
    void cough(void);
    
    int main(void)
    {
        for (int i = 0; i < 3; i++)
        {
            cough();
        }
    }
    
    void cough(void)
    {
        printf("cough\n");
    }
    ```
    
    ```c
    #include <stdio.h>
    
    void cough(int n);
    
    int main(void)
    {
        for (int i = 0; i < 3; i++)
        {
            cough();
        }
    }
    
    void cough(int n)
    {
        for (int i = 0; i < n; i++)
        {
            printf("cough\n");
        }
    }
    ```
    
</br>

## 하드웨어의 한계

- RAM :모든 프로그램이 실행 중 저장되는 곳. 컴퓨터가 여러 일을 한 번에 할 때 기억하기 위해 사용.
    - 메모리의 용량은 무한하지 않기 때문에, 때때로 프로그램에서 우리가 의도하지 않은 오류가 발생하기도 함
- 부동 소수점 부정확성
    
    ```c
    #include <cs50.h>
    #include <stdio.h>
    
    int main(void)
    {
        float x = get_float("x: ");
        float y = get_float("y: ");
        
        printf("x / y = %.50f\n", x / y);
    }
    
    '''
    x: 1
    y: 10
    x / y = 0.10000000149011611938476562500000000000000000000000
    '''
    # float 에서 저장 가능한 비트 수가 유한하기 때문에 다소 부정확한 결과를 내게 됨
    ```
    
- 정수 오버플로우
    
    ```c
    #include <stdio.h>
    #include <unistd.h>
    
    int main(void)
    {
        for (int i = 1; ; i *= 2)
        {
            printf("%i\n", i);
            sleep(1);
        }
    }
    
    ...
    1073741824
    overflow.c:6:25: runtime error: signed integer overflow: 1073741824 * 2 cannot be represented in type 'int'
    -2147483648
    0
    0
    ...
    # int에서는 32개의 비트가 다였기 때문에 그 이상의 숫자는 저장할 수 없게 
    ```
    
- 기타 오버플로우 문제
    - Y2K 문제: 1999년에 큰 이슈가 되었던 문제로, 연도를 마지막 두 자리수로 저장했던 관습 때문에 새해가 오면 ‘99’에서 ‘00’으로 정수 오버플로우가 발생하고, 새해가 2000년이 아닌 1900년으로 인식된다는 문제. 결국 수백만 달러를 투자해 더 많은 메모리를 활용해 해결해야만 했음.
    - 보잉787 문제: 구동 후 248일이 지나면 소프트웨어의 변수가 오버플로우되어 모든 전력을 잃는 문제. 이를 해결하기 위해 주기적으로 재가동을 하여 변수를 다시 0으로 리셋해야 했음.
    - 따라서 다루고자 하는 데이터 값의 범위를 유의하며 프로그램을 작성하는 것이 중요.