import json
from functools import wraps

def save_progress(func):
    @wraps(func)
    def wrapper(game, *args, **kwargs):
        result = func(game, *args, **kwargs)
        with open("data/save.json", "w") as f:
            json.dump({"scene": game.current_scene_id}, f)
        return result
    return wrapper

def loot_generator():
    loot = ["Sword", "Potion", "Shield", "Gold"]
    for item in loot:
        yield item
