from src.geometry.point import Point
from src.geometry.torus import Torus
from src.algorithms.router import solve_k33_on_torus
from src.visualization.visualizer import visualize_solution

'''
The complexity of the algorithm wouuld be, due to the implementation made:
Time: O(1)
Space O(1)

This is because the problem proposes an amount of 3 points connected to other 3 points,
with which the total number of paths is, and always will be, 9. Theres no need to store 
more than 9 paths and their limited segments. 

Time is constant due to the implementation based on an A* search algorithm, the algorithm
uses a recursive approach to find mid-points until its able to connect the source point with
the end point. The posible mid-points and possible bends in the path are manually limited to
5 bends/segments and mid-point positions in an 8x8 grid around the start of the current segment.

The solution is fast, although due to the greedy nature of the implemented A* algorithm it could
potentially fail with more complex point positionings, if a full A* search was realized then the 
solution could be more robust, although the time complexity would be considerably higher. 
'''

def main():
    torus = Torus(30, 30)

    # Define the locations of houses and services
    # A simple layout to start
    houses = [Point(5, 10), Point(10, 15), Point(15, 20)]
    services = [Point(25, 10), Point(25, 15), Point(10, 20)]

    print("Attempting to solve K3,3 on a torus...")
    paths = solve_k33_on_torus(houses, services, torus)

    if paths:
        print("Solution found!")
        visualize_solution(torus, houses, services, paths)
        for p in paths:
            print(p)
    else:
        print("Could not find a non-intersecting solution with the current algorithm.")

if __name__ == "__main__":
    main()


