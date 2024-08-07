from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    # Sort segments by their end points
    segments.sort(key=lambda seg: seg.end)
    
    points = []
    current_point = -float('inf')  # Initialize to a very small number

    for seg in segments:
        # If the current segment is not covered by the last point
        if current_point < seg.start:
            # Select the end of the current segment as the new point
            current_point = seg.end
            points.append(current_point)

    return points

if __name__ == '__main__':
    input = stdin.read()
    data = list(map(int, input.split()))
    
    n = data[0]
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[1::2], data[2::2])))
    
    points = optimal_points(segments)
    
    print(len(points))
    print(*points)
