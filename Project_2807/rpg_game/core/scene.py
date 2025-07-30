class Scene:
    def __init__(self, scene_id, description, choices):
        self.scene_id = scene_id
        self.description = description
        self.choices = choices

    def display(self):
        print("\n" + self.description)
        for i, (text, _) in enumerate(self.choices, 1):
            print(f"{i}. {text}")

    def get_next_scene(self, choice_index):
        return self.choices[choice_index - 1][1]
