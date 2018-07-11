class Player:

    # name = []
    # score = []

    def __init__(self):
        self.name = []
        self.score = []

    def showPlayer(self, n, s):
        self.name.append(n)
        self.score.append(s)
        print(self.name)
        print(self.score)

obj_1 = Player()
obj_1.showPlayer('Sachin', 76)

obj_2 = Player()
obj_2.showPlayer('Rahul', 56)
