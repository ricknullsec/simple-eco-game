class Mine:
    def __init__(self, name):
        self.name = name
        self.production = 100
        self.value = 1000
        self.storage = 0
    def produce(self, days):
        self.storage += self.production
        return self.name + " has produced " + str(self.production) + " having a total of " + str(self.storage) + " after " + str(days) + " days."

    def upgrade(self, muiltiplyer):
        self.production *= muiltiplyer
        print(self.name + " has been upgraded.")

class Corporation:
    pass

    
testMine = Mine("Gold Mine")

print(testMine.name)
print(testMine.produce(1))
testMine.upgrade(5)

print(testMine.produce(1))



