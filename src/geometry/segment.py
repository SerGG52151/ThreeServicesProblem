from .point import Point

class Segment:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"Segment({self.p1}, {self.p2})"

    def intersects(self, other):
        # Basic line segment intersection logic
        def orientation(p, q, r):
            val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
            if val == 0: return 0  # Collinear
            return 1 if val > 0 else 2  # Clockwise or Counterclockwise

        o1 = orientation(self.p1, self.p2, other.p1)
        o2 = orientation(self.p1, self.p2, other.p2)
        o3 = orientation(other.p1, other.p2, self.p1)
        o4 = orientation(other.p1, other.p2, self.p2)

        if o1 != o2 and o3 != o4:
            # Ignore intersections at endpoints
            if self.p1 == other.p1 or self.p1 == other.p2 or self.p2 == other.p1 or self.p2 == other.p2:
                return False
            return True

        return False
