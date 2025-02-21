import random, sys

def generateRandomPoints():                    # Generirajmo 10 naključnih točk za naslednjo vajo...
    points = []
    for i in range(1, 11):
        x = round(random.uniform(0, 100), 2)  # Naključna vrednost med 0 in 100
        y = round(random.uniform(0, 100), 2)
        points.append([x, y])
    return points


def sumXY(random_points):
    sumX = 0
    sumY = 0
    for point in random_points:
        sumX = sumX + point[0]   # koordinata x je na indexu 1  štet začne od 0;  x=0, y=1; tako ima poindeksirano
        sumY = sumY + point[1]   # koordinata y je na indexu 2
    return [sumX, sumY]


def geocenterXY(random_points):
    [sumX, sumY] = sumXY(random_points)  
    num_of_coordinates = len(random_points)
    print("Število koordinat:", num_of_coordinates)
    return [sumX/num_of_coordinates, sumY/num_of_coordinates]


def maxXY(random_points):
    maxX = 0
    maxY = 0
    for point in random_points:
        if point[0] > maxX:
            maxX = point[0]     # x je na prvem mestu seznama in ima index 0,
        if point[1] > maxY:
            maxY = point[1]     # y je na drugem mestu v seznamu in ima index 1
    return [maxX, maxY]


def minXY(random_points):
    minX = sys.float_info.max
    minY = sys.float_info.max
    for point in random_points:
        if point[0] < minX:
            minX = point[0]     # x je na prvem mestu seznama in ima index 0,
        if point[1] < minY:
            minY = point[1]     # y je na drugem mestu v seznamu in ima index 1
    return [minX, minY]


def translationXY(random_points, translation_vector):
    for point in random_points:
        point[0] = point[0] + translation_vector[0]
        point[1] = point[1] + translation_vector[1]
    return random_points


if __name__ == "__main__":                    # Glavni program
    random_points = generateRandomPoints()    # Generiramo 10 poljubnih točk za naslednjo vajo...
    for point in random_points:
        print(point)
    [sumX, sumY] = sumXY(random_points)       
    print("sumX: ", sumX, "sumY: ", sumY)
    [averageX, averageY] = geocenterXY(random_points)
    print("averageX: ", averageX, "averageY: ", averageY)
    [maxX, maxY] = maxXY(random_points)
    print("maxX: ", maxX, "maxY: ", maxY)
    [minX, minY] = minXY(random_points)
    print("minX: ", minX, "minY: ", minY)
    translation_vector = [100, 100]
    translated_random_points = translationXY(random_points, translation_vector)
    for point in translated_random_points:
        print(point)