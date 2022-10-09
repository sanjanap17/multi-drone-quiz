import time
from result import *
import math
import numpy as np
import heapq

def valid(x,y,M,N):
    if ((x<M and 0<=x) and (0<=y and y<N)):
        return True
    else:
        return False

def remove(q,indices):
    try:
        q.remove(indices)
    except ValueError:
        pass

def esdf(M, N, obstacle_list):
    """
    :param M: Row number
    :param N: Column number
    :param obstacle_list: Obstacle list
    :return: An array. The value of each cell means the closest distance to the obstacle
    """
    distance = [[2**16 for y in range(N)] for x in range(M)] 
    roots = [[2**16 for y in range(N)] for x in range(M)] 
    q = []
    eight_neighbor_adj =[[1,0],[0,1],[1,1],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1]]
    for i in range(len(obstacle_list)):
        obs = obstacle_list[i]
        distance[obs[0]][obs[1]] = 0
        roots[obs[0]][obs[1]] = obs
        heapq.heappush(q, obs)
    
    while (len(q) != 0):
        curr = heapq.heappop(q)
        for i in eight_neighbor_adj:
            x = curr[0] + i[0]
            y = curr[1] + i[1]
            indices = []
            indices.append(x)
            indices.append(y)
            if valid(x,y,M,N):
                obstacle = roots[curr[0]][curr[1]]
                curr_dist = math.sqrt((indices[0]-obstacle[0])**2 + (indices[1]-obstacle[1])**2)
                if curr_dist < distance[indices[0]][indices[1]]:
                    if distance[indices[0]][indices[1]] != 2^16:
                        remove(q,indices)
                    if curr_dist.is_integer():
                        curr_dist = int(curr_dist)
                    distance[x][y] = (curr_dist)
                    roots[x][y] = obstacle
                    heapq.heappush(q,indices)
    return(distance)
   
    pass


if __name__ == '__main__':
    st = time.time()
    for _ in range(int(2e4)):
        assert np.array_equal(esdf(M=3, N=3, obstacle_list=[[0, 1], [2, 2]]), res_1)
        assert np.array_equal(esdf(M=4, N=5, obstacle_list=[[0, 1], [2, 2], [3, 1]]), res_2)

    et = time.time()
    print(et-st)
