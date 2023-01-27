
## 새로 학습한 내용

- json 파일 불러오기 - 절대경로, 상대경로 주의
    - 절대경로
        
        ```python
        if __name__ == '__main__':
            # movie_json = open('data/movie.json', encoding='utf-8')
            # movie_dict = json.load(movie_json)
            
            file_url='C:/Users/SSAFY/Desktop/01_pjt/code/data/movie.json'
            with open(file_url, 'r', encoding="utf-8") as movie_json:
                movie_dict = json.load(movie_json)
            
            pprint(movie_info(movie_dict))
        ```
        
    - 상대경로 : 터미널 현재 경로 확인
        
        ```python
        import json
        
        movie = open('examples/sample.json', encoding='utf-8')
        movie_detail = json.load(movie)
        
        print(movie_detail)
        ```
        
- Dict 활용 관련
    - Dictionary 순회 시 Del 을 통해 원소를 삭제하면 순회 중 원소 변경으로 인해 오류 뜸
        - Temp = dict로 동일한 딕셔너리 만들고 다른 딕셔너리의 원소를 삭제하더라도 call by reference 방식으로 호출되기 때문에 Temp 역시 구조가 변경됨에 주의
    - key를 통해 value에 접근하는 것이 value를 통해 key에 접근하는 것보다 쉬움
    - key값이 동일하다면 원소 추가하더라도 덮어씌워지므로, item으로 원소를 추가하는 것이 바람직
- 정렬
    - list는 sort 함수, dictionary는 sorted 함수를 활용한다!

</br>

## 어려웠던 부분

- Dict 활용법, 정렬 활용

</br>

## 느낀 점

- 파일명을 정할 때 신중해야 함
    - 개별 파일의 고유 속성을 드러내주는 정보를 포함하는 것이 바람직