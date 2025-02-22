from point2d import Point2d
from Point2dListOperations import Point2dList

p1 = Point2d(1, 2.0, 3.0)
p2 = Point2d(2, 4.5, 6.7)
p3 = Point2d(3, 8.1, 9.3)
p4 = Point2d(4, 5.4, 5.0)
listOfPoints = [p1, p2, p3, p4]

points = Point2dList(listOfPoints)

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
print("Translated points: [+100, +100]")
translated_random_points.printListOfPoints()
