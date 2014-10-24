class CircularList:
    def __init__(self, node):
        self.head = node
        self.head.suivant = self.head
        self.head.precedent = self.head

        self.tail = self.head

        self.current = self.head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.head:
            self.current = self.current.suivant
            return self.head

        else:
            res = self.current
            self.current = self.current.suivant
            return res

    def insertAfter(self, node):
        node.suivant = self.head
        node.precedent = self.tail

        self.tail.suivant = node

        self.head.precedent = node

        self.tail = node

    def remove(self, node):
        if node == self.head:
            self.head = node.suivant

        if node == self.tail:
            self.tail = node.precedent

        node.precedent.suivant = node.suivant
        node.suivant.precedent = node.precedent
        del node


    def length(self):
        length = 1
        terminee = False
        node = self.head
        while not terminee:
            if node.suivant != self.head:
                node = node.suivant
                length += 1
            else:
                terminee = True

        return length