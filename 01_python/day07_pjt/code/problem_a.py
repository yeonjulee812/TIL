import requests

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': 'a62cf9c56e11cd1fba54eb65dc144472',
        'language': 'ko',
        'region': 'KR'
    }

    # 요청 및 응답
    response = requests.get(BASE_URL + path, params=params).json()
    # 결과
    return len(response.get('results'))

if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
