import json

def dec_movies(movies):
    movie_month = {}
    for movie_dict in movies:
        movie_num = movie_dict['id']
        path = 'data/movies/'+ str(movie_num) + '.json'
        movie_json = open(path, encoding='utf-8')
        movie_dict = json.load(movie_json)
        
        movie_month[movie_dict['title']] = movie_dict['release_date'][5:7]
    
    movie_li = []
    for key, value in movie_month.items():
        if value == '12':
            movie_li.append(key)

    return movie_li

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
