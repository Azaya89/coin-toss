from random import choice


class Coin:
    """Creating a coin with 2 sides."""

    def __init__(self, sides=["head", "tail"]):
        self.sides = sides

    def toss(self):
        """Simulate tossing the coin."""
        return choice(self.sides)
