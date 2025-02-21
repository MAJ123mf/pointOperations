import random                                 # uvozimo knjižnico random, da bo ukaz random deloval

class Point2d:
    def __init__(self, pointNumber, x:float, y:float):
        self.pointType = "Point2d"
        self.setPointNumber(pointNumber)
        self.setX(x)
        self.setY(y)

    def setPointNumber(self, pointNumber):
        self.pointNumber = pointNumber


    def setX(self, x):
        if isinstance(x, str):  # Če je x string, ga poskusimo pretvoriti
            try:
                x = float(x)  
            except ValueError:
                print(f"Opozorilo: '{x}' ni veljavno število. X ostaja nespremenjen.")
                return  # Funkcija se prekine, x ostane nespremenjen
        if not isinstance(x, (int, float)):  
            print(f"Opozorilo: Neveljaven tip podatka {type(x).__name__}. X ostaja nespremenjen.")
            return  
        if x < 0:  
            print("Opozorilo: X mora biti pozitiven! X ostaja nespremenjen.")
            return  # Funkcija se prekine, x ostane nespremenjen
        self.x = x  # Če je vse pravilno, nastavimo X


    def setY(self, y):
        if isinstance(y, str): 
            try:
                y = float(y)  
            except ValueError:
                print(f"Opozorilo: '{y}' ni veljavno število. Y ostaja nespremenjen.")
                return  # Funkcija se prekine, y ostane nespremenjen
        if not isinstance(y, (int, float)):  
            print(f"Opozorilo: Neveljaven tip podatka {type(y).__name__}. Y ostaja nespremenjen.")
            return  
        if y < 0:  
            print("Opozorilo: Y mora biti pozitiven! Y ostaja nespremenjen.")
            return  # Funkcija se prekine, y ostane nespremenjen
        self.y = y  # Če je vse pravilno, nastavimo X 


    def translate(self, transX:float, transY:float):
        self.x = self.x + transX
        self.y = self.y + transY

    def printCoordinates(self):
        print("Point:", self.pointNumber, self.x, self.y, self.pointType)

    def getAsList(self):                          # List je posebna podatkovna struktura v Pythonu
        return [self.pointNumber, self.x, self.y]
    
    def getAsDict(self):                           # dictionary je posebna podatkovna struktura v Pythonu
        return {'n': self.pointNumber, 'x': self.x, 'y': self.y}
    
    @staticmethod                                  # Staticmethod, pove, da metoda ni odvisna od class-a
    def generateRandomPoints():                    # Generirajmo 10 naključnih točk za naslednjo vajo...
        points = []
        for i in range(1, 11):
            x = round(random.uniform(0, 100), 2)  # Naključna vrednost med 0 in 100
            y = round(random.uniform(0, 100), 2)
            points.append(Point2d(i, x, y))
        return points

if __name__ == "__main__":                # Glavni program
    p1=Point2d(123, 10, 10)               # Naredi točko pointNumber=123, x=10, y=10
    p1.translate(1,1)
    p1.printCoordinates()
    print("List: ", p1.getAsList())
    print("Dictionary: ", p1.getAsDict())
    random_points = Point2d.generateRandomPoints()    # Generiramo 10 poljubnih točk za naslednjo vajo...
    for point in random_points:
        print(point.getAsList())