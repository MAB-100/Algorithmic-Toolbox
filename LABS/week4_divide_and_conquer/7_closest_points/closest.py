from collections import namedtuple
from itertools import combinations
from math import sqrt
 
Point = namedtuple('Point', 'x y')
 
def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2
 
def minimum_distance_squared(points):
    # Sort points by x-coordinate
    points.sort(key=lambda point: point.x)
 
    def closest_pair(left, right):
        if right - left <= 3:  # Base case for 3 or fewer points
            return minimum_distance_squared_naive(points[left:right])
       
        mid = (left + right) // 2
        mid_x = points[mid].x
 
        # Recursively find the smallest distance in both halves
        d1 = closest_pair(left, mid)
        d2 = closest_pair(mid, right)
 
        # Find the minimum distance
        d = min(d1, d2)
 
        # Create a strip to check points close to the dividing line
        strip = []
        for i in range(left, right):
            if abs(points[i].x - mid_x) < sqrt(d):
                strip.append(points[i])
 
        # Check the strip for closer points
        strip.sort(key=lambda point: point.y)  # Sort strip by y-coordinate
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if (strip[j].y - strip[i].y) >= sqrt(d):
                    break  # No need to check further
                d = min(d, distance_squared(strip[i], strip[j]))
 
        return d
 
    return closest_pair(0, len(points))
 
def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")
    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared, distance_squared(p, q))
    return min_distance_squared
 
if __name__ == '__main__':
    try:
        input_n = int(input())
        input_points = []
        for _ in range(input_n):
            x, y = map(int, input().split())
            input_point = Point(x, y)
            input_points.append(input_point)
 
        # Calculate the minimum distance squared
        min_distance_sq = minimum_distance_squared(input_points)
 
        # Print the square root of the minimum distance squared
        print("{:.9f}".format(sqrt(min_distance_sq)))
 
    except EOFError:
        print("Input was not provided correctly.")
    except ValueError as e:
        print(f"Invalid input: {e}")