import requests
from pprint import pprint

def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': 'a62cf9c56e11cd1fba54eb65dc144472',
        'language': 'ko',
        'region': 'KR',
        'query': title
    }

    # 영화 검색
    response = requests.get(BASE_URL + path, params=params).json()
    searched_movies = response.get('results')

    # 영화 검색가능 여부 판단
    if len(searched_movies) == 0:
        return None

    else:
        # 첫번째 영화만 가져옴
        movie = searched_movies[0]

        # 검색된 영화의 id 추출
        movie_id = movie.get('id')

        # path, 파라미터 변경
        path = path.lstrip('/search')
        recommend = str(movie_id) + '/recommendations'            
        params.pop('query')
        params.pop('region')
            
        # 추천영화 받기
        new_response = requests.get(BASE_URL + '/' + path + '/' + recommend, params = params).json()
        recommended_movies = new_response.get('results')

        # 추천여부 판단
        if recommended_movies is None:
            return []

        else:
            name_list = []
            for movie in recommended_movies:
                # 추천영화 목록 리스트 생성
                name_list.append(movie.get('title'))

            # 결과 출력
            return name_list

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성-- 전체 영화 목록 프린트
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
