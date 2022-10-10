# multi-drone-quiz
## Problem #1
ESDF calculation using Image Foresting Transform
Obstacles are considered as roots of the tree and their distance values are set to 0. The idea is to propogate outwards from the root nodes (obstacles) to the neighboring cells and compute Euclidean distance.

Reference: (https://medium.com/on-coding/euclidean-distance-transform-d37e06958216)

## Problem #2
Assumption 1: The height of the drone above the ground is known.
Assumption 2: At a discrete time step, the drone is over one cell of the grid.

Consider a grid of possible locations that the drone can fly over at the discrete time intervals. Since the obstacles do not move, create a map using ESDF as per Problem #1. When the drone is above a particular cell of the grid, the cell stores the horizontal distance to the nearest obstacle and the vertical distance of the drone is known (Assumption).  Using Pythagoras theorem, the distance between the drone and obstacle can be computed. If the obstacles and drone are in the same horizontal plane, this calculation is not needed and the distance to nearest obstacle is directly obtained from the ESDF grid.
ESDF needs to be computed only if obstacles move. As they do not move, it can be calculated once and can be used as a lookup. When the drones move, a simple calculation of the distance needs to be calculated.

## Problem #4
Divide the room (root of octree) into 8 cubes (child nodes of octree). The octree keeps track of the cubes within the room that have been occupied. 
Add the boxes to the room in decreasing order of size. The box is added to the octree node where it can fit based on the node size (Keep dividing the tree till node size is closest to the box size). If a node of the octree is filled, its child shouldn't be created since no other box can be placed there.