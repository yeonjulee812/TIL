
## 문제 A. 제공되는 영화 데이터의 인기 영화 조회

[problem_a.py](./problem_a.py)

<details>
<summary>접기/펼치기 버튼</summary>
<div markdown="1">

### Logic

- 기본 주소(BASE_URL), 원하는 주소(path), 파라미터(params)를 구분하고, `request`라이브러리의 get함수를 사용해 HTTP 요청
- [https://www.themoviedb.org/](https://www.themoviedb.org/?language=ko) 에 가입하여 전달받은 API key를 파라미터에 입력
- 응답 데이터가 JSON 포맷이므로 `json()`를 통해 dict 객체를 받음
- `len()`를 통해 영화 목록 개수 반환

</div>
</details>
<br/>

## 문제 B. 특정 조건에 맞는 인기 영화 조회

[problem_b.py](./problem_b.py)

<details>
<summary>접기/펼치기 버튼</summary>
<div markdown="1">
    
### Logic

- 문제 A에서 조회한 인기 영화 중 평점 8점 이상인 영화를 조회하기 위해, `for문`을 활용해 개별 영화의 평점 조회한 후 `if문`으로 평점 조건 적용

</div>
</details>
<br/>

## 문제 C. 특정 조건에 맞는 인기 영화 정렬

[problem_c.py](./problem_c.py)

<details>
<summary>접기/펼치기 버튼</summary>
<div markdown="1">
    
### Logic

- 인기 영화 리스트를 `sort()` 활용해 정렬하되, 파라미터(**`key`**, `reverse`)를 지정하여 dict 자료형인 개별 인자의 평점 순으로 내림차순 정렬
- List Slicing으로 평점 Top 5 영화 조회

</div>
</details>
<br/>

## 문제 D. 영화 검색 후 id 값으로 추천영화 조회

[problem_d.py](./problem_d.py)

<details>
<summary>접기/펼치기 버튼</summary>
<div markdown="1">
    
### Logic

- `if문`으로 영화 검색여부 판단 후 검색가능하면 인덱싱을 활용해 첫 번째 영화만 가져와서 id 추출
- URL의 path, 파라미터 변경 후 추천영화 조회
- 추천영화 존재 여부 판단 후 존재하면 새로운 리스트 생성해 결과 출력

### Error & Solution

- 검색가능 여부 판단 시  ***IndexError : list index out of range*가 뜸**
    - ‘검색할 수 없는 영화’를 검색할 경우 searched_movies 가 ‘[]’로 나오는데, ‘[]’는 None이 아니기 때문임
    
    ```python
    # 변경 전
    if searched_movies is None:
        return None
    else:
        movie = searched_movies[0] # IndexError
    
    # 변경 후
    if len(searched_movies) == 0:
        return None
    ```
    
- URL을 수정하는 과정에서 가독성이 떨어지는 문제
    - 별도의 파이썬 파일을 만들어 데이터 조회, (영화명) 검색 모듈을 생성하여 보완할 수 있을 것임
- `lstrip()`는 원본 데이터를 변경시키지 않으므로 변수 할당이 필요하며, `pop()`을 이용해 키를 제거할 경우 변수 할당할 필요가 없음!

</div>
</details>
<br/>

## 문제 E. 영화 검색 후 특정 조건에 맞는 출연진 조회

[problem_e.py](./problem_e.py)

<details>
<summary>접기/펼치기 버튼</summary>
<div markdown="1">
    
### Logic

- 문제 D와 같은 방식으로 영화명으로 검색되는 첫 번째 영화 데이터를 가져와서 id 추출
- cast, crew 목록 조회하되 `if문`으로 각각 id가 ‘10 미만’, department가 ‘Directing’인 조건 적용 후 인물명 리스트 생성

</div>
</details>
<br/>