# ThreeServicesProblem

The complexity of the solution wouuld be, due to the implementation made:
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