import json

# 90년대 개봉작 중 많은 수입을 올린 영화 순위
def dec_movies(movies):
    movie_revenue = {}
    movie_rank = []

    for movie_dict in movies:
        movie_num = movie_dict['id']
        path = 'data/movies/'+ str(movie_num) + '.json'
        movie_json = open(path, encoding='utf-8')
        movie_dict = json.load(movie_json)
        
        # 90년대 개봉작 추출
        if movie_dict['release_date'][2] == '9':
            movie_revenue[movie_dict['title']] = movie_dict['revenue']
    
    sorted_list = sorted(movie_revenue.items(), key = lambda item: item[1], reverse=True)
    print(sorted_list)
    
    for tp in sorted_list:
        print(type(tp))
        for i, j in tp:
            print(i)
            movie_rank.append(i)
    
    return movie_rank

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
