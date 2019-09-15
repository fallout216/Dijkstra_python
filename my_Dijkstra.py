# given a graph and a source vertex, print a list in the form as a list of node : distance
# usage: Dijkstra(graph, the source vertex)

import numpy
import sys


# find the node that is not yet in the shortest path tree set
# and has smallest distance to the source node
def min_dist(dist,sptSet):
    temp = sys.maxsize # temp is initialized as infinity
    node = 0
    for count in range(dist.size):
        if (dist[count] < temp and sptSet[count] == False):
            node = count
            temp = dist[count]
    return node

# print the result
def print_dist(dist, pred, src=0):
    print("From the source node", src)
    for count in range(dist.size):
        if src == count:
            print("to the destination node", count, "with cost =", dist[count], "\n")
        else:
            print("to the destination node", count,"with cost =", dist[count], "\n", count, end='')
            predecessor = pred[count]
            while predecessor != None:
                if predecessor == src:
                    print("<-", src)
                    break
                else:
                    print("<-", predecessor, end='')
                    predecessor = pred[predecessor]


def Dijkstra(graph, src=0):
    graph = numpy.array(graph)
    if (graph.size == 0):
        print("The graph must be a square matrix with at least 1X1 dimension.")
        return 'Error!'
    if (src < 0 or src > graph.size):
        print("The source node must be between 0 and the dimension of the graph")
        return 'Error!'
    num = graph[1].size # num = dimension
    sptSet = [False for n in range(num)] # sptSet = the shortest path tree set

    inf = sys.maxsize # inf = infinity
    dist = [inf for n in range(num)] # dist = the distance array

    dist = numpy.array(dist)
    dist[src] = 0

    # we also need a predecessor vector to print the shortest path from the source to the destination
    # first we initialize each element in pred as NONE
    pred = [None for n in range(num)]
    pred = numpy.array(pred)

    # from now on Dijkstra algorithm is implemented:
    for count in range(num):
        node = min_dist(dist,sptSet)
        sptSet[node] = True
        for neighbor in range(num):
            if (sptSet[neighbor] == False and graph[node][neighbor]>0 and (dist[node]+graph[node][neighbor]) < dist[neighbor]):
                # the next two lines are for debugging
                # print("node = " + str(node), ", dist[node] = " + str(dist[node]),
                #       ", graph[node][neighbor] = " + str(graph[node][neighbor]), ", neighbor = "+ str(neighbor))
                dist[neighbor] = dist[node]+graph[node][neighbor]

                # set the predecessor of the neighbor as the node
                pred[neighbor] = node

    #print out the result
    print_dist(dist, pred, src)



# driver

# graph = [
#     [0,9,2,4],
#     [9,0,3,1],
#     [2,3,0,1],
#     [4,1,1,0]
# ]

# graph=[ [0, 3, 0, 1, 0, 0, 0, 2, 0],
#         [3, 0, 4, 0, 0, 2, 0, 9, 0],
#         [0, 4, 0, 7, 0, 4, 0, 0, 2],
#         [1, 0, 7, 0, 3, 0, 6, 0, 0],
#         [0, 0, 0, 3, 0, 10, 0, 0, 0],
#         [0, 2, 4, 0, 10, 0, 12, 0, 0],
#         [0, 0, 0, 6, 0, 12, 0, 3, 6],
#         [2, 9, 0, 0, 0, 0, 3, 0, 2],
#         [0, 0, 2, 0, 0, 0, 6, 2, 0]
#         ];

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];

Dijkstra(graph,8)
