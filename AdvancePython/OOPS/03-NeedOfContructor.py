class Emp():

    name = []
    score = []

    def showStats(self,playerName,playerScore):
        Emp.name.append(playerName)
        Emp.score.append(playerScore)
        print(Emp.name, Emp.score)

sachin = Emp()
sachin.showStats('Sachin', 88)

kohli = Emp()
kohli.showStats('Kohli', 100)