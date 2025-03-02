class Mine:
    def __init__(self, name, owner):
        self.name = name
        self.production = 100
        self.value = 1000
        self.storage = 0
        self.owner = owner
        print(self.owner + " created new mine " + self.name + ".")
    
    def produce(self):
        self.storage += self.production
        print(self.name + " has produced " + str(self.production) + " having a total of " + str(self.storage))
    
    def upgrade(self, muiltiplyer):
        self.production *= muiltiplyer
        self.value *= muiltiplyer
        print(self.name + " has been upgraded.")

class Corporation:
    def __init__(self, name):
        self.name = name
        self.storage = 0
        self.money = 1000
        self.mines = []
        print("New corporation " + self.name + " created.")
    
    def buildMine(self, name):
        self.mines.append(Mine(name,self.name))
    

    
playerCorp = Corporation("Black Inc")
playerCorp.buildMine("Gold Mine")


for mine in playerCorp.mines:
    mine.produce()

