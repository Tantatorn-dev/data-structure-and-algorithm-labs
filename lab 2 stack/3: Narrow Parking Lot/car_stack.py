class CarStack:

    def __init__(self, list=None, space=0):
        if list == None:
            self.mySoi = []
        else:
            self.mySoi = list
        self.availableSpace = space
        self.maxSpace = space
        self.neighbourSoi = []

    def arrive(self, car):
        if self.availableSpace == 0:
            print("car %d cannot arrive : SOI FULL" % (self.maxSpace+1))
            return
        else:
            self.mySoi.append(car)
            self.availableSpace -= 1
        print("car %d arrive       space left %d" % (car, self.availableSpace))

    def depart(self, carNumber):
        if len(self.mySoi) == 0:
            print("car %d cannot depart : soi empty" % (self.maxSpace+1))
            return
        isin = False
        for i in range(len(self.mySoi)):
            outCar = self.mySoi.pop()
            if  outCar== carNumber:
                isin = True
                break
            else:
                self.neighbourSoi.append(outCar)
        for i in range(len(self.neighbourSoi)):
            self.mySoi.append(self.neighbourSoi.pop())
        if isin:
            self.availableSpace += 1
            print("car %d depart      space left %d" %
              (carNumber, self.availableSpace))
        else:
            print("car %d cannot depart: no car %d"%(carNumber,carNumber))

    def isFull(self):
        return len(self.mySoi) == self.availableSpace

    def getAvailableSpace(self):
        return len(self.mySoi)

    def printSoi(self):
        print("print soi = ", end=' ')
        print(self.mySoi)
