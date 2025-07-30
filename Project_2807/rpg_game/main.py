import json
import os
from core.player import Player
from core.scene import Scene
from core.decorators import save_progress, loot_generator

class Game:
    def __init__(self):
        self.player = Player(input("Enter your name: "))
        self.scenes = self.load_scenes()
        self.current_scene_id = self.load_saved_scene() or "start"
        self.loot_gen = loot_generator()

    def load_scenes(self):
        with open("data/scenes.json") as f:
            data = json.load(f)
            scenes = {}
            for scene_id, details in data.items():
                scenes[scene_id] = Scene(scene_id, details["description"], details["choices"])
            return scenes

    def load_saved_scene(self):
        if os.path.exists("data/save.json"):
            with open("data/save.json") as f:
                data = json.load(f)
                return data.get("scene")
        return None

    @save_progress
    def move_to_scene(self, scene_id):
        self.current_scene_id = scene_id

    def start(self):
        print(f"\nWelcome, {self.player.name}!")
        while self.current_scene_id:
            scene = self.scenes[self.current_scene_id]
            scene.display()

            if self.current_scene_id == "fight":
                self.player.take_damage(10)
                try:
                    item = next(self.loot_gen)
                    self.player.add_to_inventory(item)
                except StopIteration:
                    print("No more loot available.")

            if not scene.choices:
                print("\nGame Over.")
                break

            try:
                choice = int(input("Enter choice: "))
                if 1 <= choice <= len(scene.choices):
                    next_scene = scene.get_next_scene(choice)
                    self.move_to_scene(next_scene)
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a number.")

if __name__ == "__main__":
    game = Game()
    game.start()
