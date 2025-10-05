import heapq
from src.geometry.point import Point
from src.geometry.segment import Segment
from src.geometry.torus import Torus

def heuristic(a: Point, b: Point):
    return ((a.x - b.x)**2 + (a.y - b.y)**2)**0.5

def a_star_search(torus: Torus, start: Point, goal: Point, existing_paths: list, depth=0):
    """
    A* search on the torus.
    """
    
    if depth > 5:  # Base case to prevent infinite recursion
        return None

    # Attempt a direct connection first.
    direct_segment = torus.get_shortest_path_segment(start, goal)
    
    is_intersecting = False
    for path in existing_paths:
        for segment in path:
            # Need to check intersection on the torus, not just in the plane.
            # This means checking all 9 versions of the segment.
            for i in range(-1, 2):
                for j in range(-1, 2):
                    other_segment_variant = Segment(
                        Point(segment.p1.x + i * torus.width, segment.p1.y + j * torus.height),
                        Point(segment.p2.x + i * torus.width, segment.p2.y + j * torus.height)
                    )
                    if direct_segment.intersects(other_segment_variant):
                        is_intersecting = True
                        break
                if is_intersecting: break
            if is_intersecting: break
        if is_intersecting: break

    if not is_intersecting:
        return [direct_segment]


    for i in range(1, 8):
        for j in range(1, 8):
            mid_point = Point((start.x + i * torus.width/8) % torus.width, (start.y + j * torus.height/8) % torus.height)
            
            path1 = a_star_search(torus, start, mid_point, existing_paths, depth + 1)
            if path1:
                path2 = a_star_search(torus, mid_point, goal, existing_paths, depth + 1)
                if path2:
                    # Check if the new combined path intersects.
                    new_path = path1 + path2
                    is_intersecting = False
                    for seg1 in new_path:
                        for path in existing_paths:
                            for seg2 in path:
                                if seg1.intersects(seg2): # Simplified check
                                    is_intersecting = True
                                    break
                            if is_intersecting: break
                        if is_intersecting: break
                    
                    if not is_intersecting:
                        return new_path

    return None # No path found

def solve_k33_on_torus(houses, services, torus: Torus):
    connections = []
    for house in houses:
        for service in services:
            connections.append((house, service))
    
    paths = []
    for start, end in connections:
        path = a_star_search(torus, start, end, paths)
        if path:
            paths.append(path)
        else:
            print(f"Failed to connect {start} and {end}")
            return None
            
    return paths
