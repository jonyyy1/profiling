
import random
import numpy as np
import pandas as pd
import time


def convex_hull(points):
    points = sorted(set(points))
    if len(points) <= 3:
        return points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    hull = []

    # Start with the leftmost point
    point_on_hull = min(points, key=lambda p: (p[0], p[1]))
    while True:
        hull.append(point_on_hull)
        endpoint = points[0]
        for point in points:
            if (endpoint == point_on_hull) or (cross(hull[-1], endpoint, point) < 0):
                endpoint = point
        point_on_hull = endpoint
        if endpoint == hull[0]:
            break

    return hull


if __name__ == '__main__':

    times = np.array([100000])
    output = np.array([])
    for t in times:
        points = [(random.uniform(0, 1_000_000), random.uniform(0, 1_000_000)) for _ in range(t)]
        start = time.time()
        hull = convex_hull(points)
        end = time.time()

        output = np.append(output, end - start)

    # Save the output to a file
    df = pd.DataFrame({'time': output, 'points': times})
    df.to_csv('output.csv', index=False)
