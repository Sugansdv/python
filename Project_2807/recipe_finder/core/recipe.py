class Recipe:
    def __init__(self, name, ingredients, steps):
        self.name = name
        self.ingredients = ingredients
        self.steps = steps

    def __str__(self):
        return (
            f" Recipe: {self.name}\n"
            f" Ingredients: {', '.join(self.ingredients)}\n"
            f" Steps:\n  - " + "\n  - ".join(self.steps)
        )
