import sys, requests, json, pickle, random, os
import omdb
from django.conf import settings

class Moviemon:
    def __init__(self, infos):
        self.title = infos['Title']
        self.img = infos['Poster']
        self.director = infos['Director']
        self.year = infos['Year']
        self.plot = infos['Plot']
        self.actors = infos['Actors']
        self.rating = float(infos['imdbRating'])

    def __str__(self):
        ret = ""
        for k, v in self.__dict__.items():
            if not(len(k) >= 4 and k[:2] == "__" and k[-2:] == "__"):
                ret += k + ' : ' + str(v) + '\n'
        return ret

class Game:
    def __init__(self):
        self.moviemons = {}
        self.moviedex = {}
        self.nb_pixel = 45
        self.grid_size = 10
        self.mario_x = self.grid_size / 2
        self.mario_y = self.grid_size / 2
        self.nb_movieballs = 50
        self.slot = 0
        self.loader = False
        self.has_moved = False

    def __str__(self):
        ret = ""
        for title, movie in self.moviemons.items():
            ret += str(movie) + '\n'
        return ret

    def omdb_request(self):
        API_KEY = getattr(settings, 'API_KEY', None)
        if API_KEY is None:
            print("Error: no API_KEY in settings.py")
            exit(1)
        moviemons = getattr(settings, 'MOVIEMONS', None)
        if moviemons is None:
            print("Error: no moviemons in settings.py")
            exit(1)
        omdb.set_default('apikey', API_KEY)
        for movie in moviemons:
            wp_call = omdb.request(t=movie)
            if wp_call.status_code != 200:
                print("Erreur HTTP, code ", str(wp_call.status_code))
                exit(1)
            infos_json = wp_call.json()
            if infos_json and 'Error' in infos_json.keys():
                print('Error: ', infos_json['Error'])
            else:
                self.moviemons[infos_json['Title']] = Moviemon(infos_json)

    def dump(self, nb=-1):
        if nb == -1 :
            pickle_name = getattr(settings, "PICKLE_NAME", None)
            if pickle_name is None:
                pickle_name = os.path.join(settings.BASE_DIR, 'infos.pickle')
        else:
            pickle_name = os.path.join(settings.SAVE_DIR, 'slot'+ str(chr(nb + 97)) + '_' + str(self.get_strength()) + '.mmg')
        with open(pickle_name, 'wb') as fd:
            tmp = self.__dict__
            to_dump = {}
            to_dump['moviemons'] = tmp['moviemons']
            to_dump['moviedex'] = tmp['moviedex']
            to_dump['nb_pixel'] = tmp['nb_pixel']
            to_dump['grid_size'] = tmp['grid_size']
            to_dump['mario_x'] = tmp['mario_x']
            to_dump['mario_y'] = tmp['mario_y']
            to_dump['nb_movieballs'] = tmp['nb_movieballs']
            to_dump['slot'] = tmp['slot']
            to_dump['loader'] = tmp['loader']
            to_dump['has_moved'] = tmp['has_moved']
            pickle.dump(to_dump, fd)

    def get_random_movie(self):
        key = random.choice(list(self.moviemons.keys()))
        return self.moviemons[key]

    def get_strength(self):
        return len(self.moviedex)

    def get_movie(self, moviemon):
        if moviemon in self.moviemons.keys():
            return self.moviemons[moviemon].__dict__
        elif moviemon in self.moviedex.keys():
            return self.moviedex[moviemon].__dict__
        else:
            return None

    @staticmethod
    def load(pickle_name):
        if not os.path.exists(pickle_name):
            game = Game()
            game.dump()
            return game
        with open(pickle_name, 'rb') as fd:
            game_dict = pickle.load(fd)
        game = Game()
        game.moviemons = game_dict['moviemons']
        game.moviedex = game_dict['moviedex']
        game.nb_pixel = game_dict['nb_pixel']
        game.grid_size = game_dict['grid_size']
        game.mario_x = game_dict['mario_x']
        game.mario_y = game_dict['mario_y']
        game.nb_movieballs = game_dict['nb_movieballs']
        game.slot = game_dict['slot']
        game.loader = game_dict['loader']
        game.has_moved = game_dict['has_moved']
        return game

    @staticmethod
    def load_default_settings():
        game = Game()
        game.omdb_request()
        game.moviedex = {}
        game.grid_size = getattr(settings, 'GRID_SIZE', None)
        if game.grid_size is None:
            game.grid_size = 10
        game.size = 450 / game.grid_size
        game.mario_x = getattr(settings, 'MARIO_X', None)
        if game.mario_x is None:
            game.mario_x = game.grid_size / 2
        game.mario_y = getattr(settings, 'MARIO_Y', None)
        if game.mario_y is None:
            game.mario_y = game.grid_size / 2
        game.nb_movieballs = getattr(settings, 'NB_MOVIEBALLS', None)
        if game.nb_movieballs is None:
            game.nb_movieballs = 50
        return game


