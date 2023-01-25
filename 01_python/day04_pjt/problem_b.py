import json
from pprint import pprint

def movie_info(movie, genres):
    
    new_data = {
        'id': movie.get('id'),
        'title': movie.get('title'),
        'poster_path': movie.get('poster_path'),
        'vote_average': movie.get('vote_average'),
        'overview': movie.get('overview'),
        'genre_names': movie.get('genre_ids')
    }

    for genre_dict in genres:
        for index, id in enumerate(new_data['genre_names']):
            if id == genre_dict['id']:
                new_data['genre_names'][index] = genre_dict['name']
    
    return new_data
    
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
