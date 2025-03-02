class Mine:
    def __init__(self, name):
        self.name = name
        self.production = 100
        self.value = 1000
        self.storage = 0
    def produce(self, days):
        self.storage += self.production
        print(self.name + " has produced " + str(self.production) + " having a total of " + str(self.storage) + " after " + str(days) + " days.")

    def upgrade(self, muiltiplyer):
        self.production *= muiltiplyer
        self.value *= muiltiplyer
        print(self.name + " has been upgraded.")

class Corporation:
    pass

    
testMine = Mine("Gold Mine")


testMine.produce(1)
testMine.upgrade(5)

testMine.produce(1)



