from Node import Node

class Joueur(Node):
    def __init__(self, name):
        super(self.__class__, self).__init__()
        self.name = name