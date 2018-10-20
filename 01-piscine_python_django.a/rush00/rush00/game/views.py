import os, pickle, random
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from .game import Game

def init(request):
    pickle_name = get_pickle_name()
    print(pickle_name)
    if os.path.exists(pickle_name):
        print("coucou")
        os.remove(pickle_name)
    return render(request, 'game/base.html')

def options(request):
    return render(request, 'game/options.html')

def battle(request, moviemon):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    moviemon = game.moviemons[moviemon]
    C = float(min(90., max(1., 50. - (moviemon.rating * 10.) + (game.get_strength() * 5.))))
    is_catched = random.choices([False, True], [1. - C / 100., C / 100.])[0]
    game.dump()
    return render(request, 'game/battle.html', {"moviemon": moviemon,
        "is_catched": is_catched, "A_actif": True, "game": game, "C" : C, "strength": str(game.get_strength())})

def battle_A(request, moviemon):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.nb_movieballs -= 1
    moviemon = game.moviemons[moviemon]
    C = float(min(90., max(1., 50. - (moviemon.rating * 10.) + (game.get_strength() * 5.))))
    is_catched =  random.choices([False, True], [1. - C / 100., C / 100.])[0]
    if is_catched:
        game.moviedex[moviemon.title] = moviemon
        del game.moviemons[moviemon.title]
        if len(game.moviemons) == 0:
            os.remove(pickle_name)
            return render(request, 'game/init.html')
    A_actif = True if (not is_catched and game.nb_movieballs > 0) else False
    game.dump()
    return render(request, 'game/battle.html', {"moviemon": moviemon,
        "is_catched": is_catched, "A_actif": A_actif, "game": game, "C" : C, "strength": str(game.get_strength()), "not_begin": True})

def moviedex(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    list_pokemon = [m for m in game.moviedex.values()]
    name = list_pokemon[game.slot].title if len(list_pokemon) > 0 else ""
    return render(request, 'game/moviedex.html', {"moviedex": list_pokemon, 'pos': game.slot + 1, 'name': str(name)})

def moviedex_up(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.slot = max(game.slot - 1, 0)
    game.dump()
    list_pokemon = [m for m in game.moviedex.values()]
    name = list_pokemon[game.slot].title if len(list_pokemon) > 0 else ""
    return redirect('/moviedex')

def moviedex_down(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.slot = min(game.slot + 1, len(game.moviemons) - 1)
    game.dump()
    list_pokemon = [m for m in game.moviedex.values()]
    name = list_pokemon[game.slot].title if len(list_pokemon) > 0 else ""
    return redirect('/moviedex')

def details(request, moviemon):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    return render(request, 'game/details.html', {"moviemon": game.moviedex[moviemon]})

def worldmap(request):
    pickle_name = get_pickle_name()
    if os.path.exists(pickle_name):
        game = Game.load(pickle_name)
    else:
        game = Game.load_default_settings()
    game.slot = 0
    game.loader = False
    has_moved = game.has_moved
    game.has_moved = False
    game.dump()
    return render(request, 'game/worldmap.html', get_worldmap_params(game, has_moved))

def load(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.dump()
    return render(request, 'game/load.html', get_load_save_params(game))

def load_A(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    slots_name = ['a', 'b', 'c']
    slot_name = slots_name[game.slot]
    slot_name = "slot" + slot_name
    save_dir = getattr(settings, 'SAVE_DIR', os.path.join(settings.BASE_DIR, 'saved_game'))
    pickle_to_load = [os.path.join(save_dir, elem) for elem in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, elem)) and slot_name in elem][0]
    game = Game.load(pickle_to_load)
    game.loader = True
    game.dump()
    return redirect('/options/load')
    #return render(request, 'game/load.html', get_load_save_params(game))

def load_up(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.slot = max(game.slot - 1, 0)
    game.dump()
    return redirect('/options/load')

def load_down(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.slot = min(game.slot + 1, 2)
    game.dump()
    return redirect('/options/load')

def get_pickle_name():
    pickle_name = getattr(settings, "PICKLE_NAME", None)
    if pickle_name is None:
        pickle_name = os.path.join(settings.BASE_DIR, 'infos.pickle')
    return pickle_name

def up(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.has_moved = True if game.mario_y > 0 else False
    game.mario_y = max(0, game.mario_y - 1)
    game.dump()
    return redirect('/worldmap')

def down(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.has_moved = True if game.mario_y < game.grid_size - 1 else False
    game.mario_y = min(game.grid_size - 1, game.mario_y + 1)
    game.dump()
    return redirect('/worldmap')

def left(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.has_moved = True if game.mario_x > 0 else False
    game.mario_x = max(0, game.mario_x - 1)
    game.dump()
    return redirect('/worldmap')

def right(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.has_moved = True if game.mario_x < game.grid_size - 1 else False
    game.mario_x = min(game.grid_size - 1, game.mario_x + 1)
    game.dump()
    return redirect('/worldmap')

def save(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.dump()
    return render(request, 'game/save.html', get_load_save_params(game))

def save_A(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.dump(game.slot)
    return redirect('/options/save_game')

def save_B(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.slot = 0
    game.dump()
    return redirect('/options')

def save_up(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.slot = max(game.slot - 1, 0)
    game.dump()
    return redirect('/options/save_game')

def save_down(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.slot = min(game.slot + 1, 2)
    game.dump()
    return redirect('/options/save_game')

def get_pickle_name():
    pickle_name = getattr(settings, "PICKLE_NAME", None)
    if pickle_name is None:
        pickle_name = os.path.join(settings.BASE_DIR, 'infos.pickle')
    return pickle_name

def get_worldmap_params(game, has_moved):
    moviemon_name = ""
    actions = ['nothing', 'movieball', 'moviemon']
    weights = [0.5, 0.25, 0.25] if has_moved else [1, 0, 0]
    action = random.choices(actions, weights)[0]
    if action == "movieball":
        game.nb_movieballs += 1
    elif action == "moviemon":
        moviemon_name = game.get_random_movie().title
    game.dump()
    return {
        'mario_px_x' : str(game.mario_x * game.nb_pixel),
        'mario_px_y' : str(game.mario_y * game.nb_pixel),
        'nb_pixel' : str(game.nb_pixel),
        'nb_movieballs' : game.nb_movieballs,
        'action' : action,
        'moviemon_name' : moviemon_name,
    }

def get_load_save_params(game):
    slots = {}
    slots['pos'] = game.slot
    slots['loader'] = game.loader
    slots_name = ['a', 'b', 'c']
    for slot_name in slots_name:
        slots[slot_name] = {}
    slots['a']
    save_dir = getattr(settings, 'SAVE_DIR', os.path.join(settings.BASE_DIR, 'saved_game'))
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    files = [os.path.join(save_dir, elem) for elem in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, elem))]
    for elem in files:
        for slot_name in slots_name:
            if 'slot' + slot_name in elem:
                game = Game.load(elem)
                slots[slot_name]['dex_number'] = len(game.moviedex)
                slots[slot_name]['mons_number'] = slots[slot_name]['dex_number'] + len(game.moviemons)
    return slots
