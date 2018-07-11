class Emp():

    # Constructor
    def __init__(self):
        self.name = []
        self.score = []

    def showStats(self,playerName,playerScore):
        self.name.append(playerName)
        self.score.append(playerScore)
        print(self.name, self.score)

sachin = Emp()
sachin.showStats('Sachin', 88)

kohli = Emp()
kohli.showStats('Kohli', 100)