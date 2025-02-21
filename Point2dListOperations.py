import sys
from point2d import Point2d

class Point2dList:                  # new class, as LIST of points2d
    def __init__(self):
        self.points = []            # on start LIST is empty


    def add_point(self, point: Point2d):
        """Dodajanje točke v seznam"""
        if isinstance(point, Point2d):
            self.points.append(point)
        else:
            raise TypeError("Only Point2d objects can be added.")

    def remove_point(self, pointNumber):
        """Odstranitev točke glede na njeno številko"""
        self.points = [p for p in self.points if p.pointNumber != pointNumber]

    def get_point(self, pointNumber):
        """Dobi točko na podlagi številke"""
        for p in self.points:
            if p.pointNumber == pointNumber:
                return p
        return None  # Če točka ne obstaja

    def __len__(self):
        """Vrne število točk v seznamu"""
        return len(self.points)

    def __getitem__(self, index):
        """Omogoča dostop do točk po indeksu kot pri običajnem seznamu"""
        return self.points[index]

    def __iter__(self):
        """Omogoča iteracijo čez seznam točk"""
        return iter(self.points)
    
    def printListOfPoints(self):
        for point in points:
            print("Point:", (point.getAsList()))


    def sum_XY(self):
        sumX = 0
        sumY = 0
        for point in points:
            sumX = sumX + point.x   # tu sedaj imamo point.x ker je Point2d podatkovni tip
            sumY = sumY + point.y  
        return [sumX, sumY]
    
    def geocenter_XY(self):
        [sumX, sumY] = points.sum_XY()
        num_of_coordinates = len(points)
        print("Number of points:", num_of_coordinates)
        return [sumX/num_of_coordinates, sumY/num_of_coordinates]
    

    def max_XY(self):
        maxX = 0
        maxY = 0
        for point in points:
            if point.x > maxX:
                maxX = point.x     
            if point.y > maxY:
                maxY = point.y     
        return [maxX, maxY]


    def min_XY(self):
        minX = sys.float_info.max
        minY = sys.float_info.max
        for point in points:
            if point.x < minX:
                minX = point.x   
            if point.y < minY:
                minY = point.y    
        return [minX, minY]


    def translation_XY(self, translation_vector):
        for point in points:
            point.x = point.x + translation_vector[0]
            point.y = point.y + translation_vector[1]
        return points
...



if __name__ == "__main__":                # Glavni program
    points = Point2dList()
    points.add_point(Point2d(1, 2.0, 3.0))
    points.add_point(Point2d(2, 4.5, 6.7))
    points.add_point(Point2d(3, 8.1, 9.3))
    points.add_point(Point2d(4, 5.4, 5.0))
    print(points)  # Prikaz vseh točk
    points.printListOfPoints()
    [sumX, sumY] = points.sum_XY()            # points so instanca objekta Point2dList sum_XY je metoda istega objekta zato klic points.sumXY()
    print("sumX: ", sumX, "sumY: ", sumY)
    [averageX, averageY] = points.geocenter_XY()
    print("averageX: ", averageX, "averageY: ", averageY)
    [maxX, maxY] = points.max_XY()
    print("maxX: ", maxX, "maxY: ", maxY)
    [minX, minY] = points.min_XY()
    print("minX: ", minX, "minY: ", minY)
    translation_vector = [100, 100]
    translated_random_points = points.translation_XY(translation_vector)
    translated_random_points.printListOfPoints()
 

    # print("Točka 2: ", points.get_point(2).getAsList())  # Pridobi točko št. 2
    # points.remove_point(1)                               # Odstrani točko št. 1
    # print("We have deleted point 1.")
    # points.printListOfPoints();