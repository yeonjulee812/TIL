import requests
from pprint import pprint

def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie/'
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
        credits = str(movie_id) + '/credits'          
        params.pop('query')
        params.pop('region')

        # 상세정보 검색
        new_response = requests.get(BASE_URL + '/' + path + credits, params = params).json()
            
        # cast, crew 목록 생성
        cast_list = []
        crew_list = []
        for cast in new_response.get('cast'):
            if cast.get('cast_id') < 10:
                cast_list.append(cast.get('name'))
        for crew in new_response.get('crew'):
            if crew.get('department') == 'Directing':
                crew_list.append(crew.get('name'))

        # 연출진 목록 반환
        credits_dict = {}
        credits_dict['cast'] = cast_list
        credits_dict['crew'] = crew_list
        return credits_dict

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None