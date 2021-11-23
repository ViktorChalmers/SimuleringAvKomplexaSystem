import numpy as np

class Person:
    def __init__(self, state:str, lattice: int):
        if isinstance(lattice, int):
            self.position = np.random.randint(lattice + 1, size=2)
        else:
            print("Oops, unaccepted lattice")
        if state == "infected":
            self.state = state
        elif state == "immune":
            self.state = state
        elif state == "recovered":
            self.state = state
        elif state == "suspectible":
            self.state = state
        elif state == "dead":
            self.state = state
        else:
            print("Oops, unaccepted state")

    def updatePosition(self, position: np.ndarray):
        if isinstance(position, np.ndarray):
            self.position = position
        else:
            print("Oops, expected a ndarray")

    def move(self,direction,lattice):
        if direction == "right" and self.position[0]<lattice:
            self.position[0] += 1
        if direction == "left" and self.position[0] > 0:
            self.position[0] += -1
        if direction == "up" and self.position[1] < lattice:
            self.position[1] += 1
        if direction == "down" and self.position[1] > 0:
            self.position[1] += -1

    def updateState(self,state: str):
        if state == "infected":
            self.state = state
        elif state == "immune":
            self.state = state
        elif state == "recovered":
            self.state = state
        elif state == "suspectible":
            self.state = state
        elif state == "dead":
            self.state = state
        else:
            print("Oops, unaccepted state")


