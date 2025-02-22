import random
from point2d import Point2d

class Point3d(Point2d):
    def __init__(self, pointNumber, x: float, y: float, z: float):
        super().__init__(pointNumber, x, y)
        self.setZ(z)
        self.pointType = "Point3d"

    def setZ(self, z):
        if isinstance(z, str):
            try:
                z = float(z)
            except ValueError:
                print(f"Opozorilo: '{z}' ni veljavno število. Z ostaja nespremenjen.")
                return
        if not isinstance(z, (int, float)):
            print(f"Opozorilo: Neveljaven tip podatka {type(z).__name__}. Z ostaja nespremenjen.")
            return
        if z < 0:
            print("Opozorilo: Z mora biti pozitiven! Z ostaja nespremenjen.")
            return
        self.z = z

    def translate(self, transX: float, transY: float, transZ: float):
        super().translate(transX, transY)
        self.z += transZ

    def printCoordinates(self):
        print("Point:", self.pointNumber, self.x, self.y, self.z, self.pointType)

    def getAsList(self):
        return [self.pointNumber, self.x, self.y, self.z]

    def getAsDict(self):
        return {'n': self.pointNumber, 'x': self.x, 'y': self.y, 'z': self.z}

    @staticmethod
    def generateRandomPoints():
        points = []
        for i in range(1, 11):
            x = round(random.uniform(0, 100), 2)
            y = round(random.uniform(0, 100), 2)
            z = round(random.uniform(0, 100), 2)
            points.append(Point3d(i, x, y, z))
        return points

if __name__ == "__main__":
    p1 = Point3d(123, 10, 10, 10)
    p1.translate(1, 1, 1)
    p1.printCoordinates()
    print("List:", p1.getAsList())
    print("Dictionary:", p1.getAsDict())
    random_points = Point3d.generateRandomPoints()
    for point in random_points:
        print(point.getAsList())
