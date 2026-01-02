from __future__ import annotations
import math


class Point:

    points = []

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        Point.points.append(self)

    def distance_to_origin(self) -> float:
        return round(math.sqrt(self.x**2 + self.y**2), 2)

    def distance_to_point(self, others: Point) -> float:
        return round(math.sqrt((self.x - others.x)**2 + (self.y - others.y)**2), 2)

    def distance_to_x_axis(self) -> float:
        return abs(self.y)

    def distance_to_y_axis(self) -> float:
        return abs(self.x)

    def find_closest_point(self) -> Point:
        closest_point = None
        closest_distance = None
        for point in Point.points:
            new_distance = self.distance_to_point(point)
            if point is self:
                continue
            else:
                if closest_distance is None:
                    closest_distance = new_distance
                    closest_point = point
                elif new_distance < closest_distance:
                    closest_point = point
                    closest_distance = new_distance
        return closest_point
