import json
from pprint import pprint

def movie_info(movies, genres):
    movie_list = []
    for movie in movies:
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
        
        movie_list.append(new_data)  
    return movie_list

if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
