import json

def max_revenue(movies):
    movie_revenue = {}
    for movie_dict in movies:
        movie_num = movie_dict['id']
        path = 'data/movies/'+ str(movie_num) + '.json'
        movie_json = open(path, encoding='utf-8')
        movie_dict = json.load(movie_json)
        
        movie_revenue[movie_dict['revenue']] = movie_dict['title']

    for key in movie_revenue.keys():
        if key == max(movie_revenue.keys()):
            return movie_revenue[key]

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
