#Execute the app.py file to get the output
import maze
import copy
def logic(src, obs, des):
    graph, size = copy.deepcopy(maze.return_maze())
    
    def min_dist(dist, sp_set):
        min = 10**10
        global min_index
        for v in range(size):
            if sp_set[v] == False and dist[v]<=min:
                min = dist[v]
                min_index = v
        return min_index

    parent = [-2 for i in range(size)]
    for x in obs:
        for y in range(size):
            graph[y][x] = 0
    dist = [10**10 for i in range(size)]
    sp_set = [False for i in range(size)]
    dist[src] = 0
    parent[src] = -1

    for u in range(size-1):
        u = min_dist(dist,sp_set)
        sp_set[u]=True
        for v in range(size):
            if sp_set[v] is False and graph[u][v]!=0 and dist[u] != 10**10 and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u
    
    def ancestor(dest):
        l1 = []
        stop = dest
        while parent[stop] != -1:
            l1.append(parent[stop])
            stop = parent[stop]
        return l1
    dest_parent = ancestor(des)
    return dest_parent