from .point import Point
from .segment import Segment
import itertools

class Torus:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_shortest_path_segment(self, p1: Point, p2: Point) -> Segment:
        """
        Gets the shortest segment between two points on the torus,
        considering wrap-around.
        """
        shortest_dist_sq = float('inf')
        best_p2_variant = p2

        for i in range(-1, 2):
            for j in range(-1, 2):
                p2_variant = Point(p2.x + i * self.width, p2.y + j * self.height)
                dist_sq = (p1.x - p2_variant.x)**2 + (p1.y - p2_variant.y)**2
                if dist_sq < shortest_dist_sq:
                    shortest_dist_sq = dist_sq
                    best_p2_variant = p2_variant
        
        return Segment(p1, best_p2_variant)

    def wrap_point(self, p: Point) -> Point:
        return Point(p.x % self.width, p.y % self.height)

    def wrap_segment(self, seg: Segment):
        """
        Returns a list of segments representing the wrapped segment on the torus.
        This can be complex if the segment crosses the boundaries multiple times.
        For simplicity, we'll handle single crossings for now.
        """
        p1 = seg.p1
        p2 = seg.p2
        
        segments = []

        segments.append(Segment(self.wrap_point(p1), self.wrap_point(p2)))
        
        return segments
