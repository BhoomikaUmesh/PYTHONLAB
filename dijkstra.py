import heapq

def dijkstra(graph,start):
    distances={node: float('inf') for node in graph}
    distances[start]=0
    heap=[(0,start)]

    while heap:
        current_dist,current_node=heapq.heappop(heap)
        if current_dist>distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance=current_dist+weight
            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(heap,(distance,neighbor))
    return distances
def find_optimal_route(graph, start, destination):
    distances=dijkstra(graph, start)
    if distances[destination]==float('inf'):
        return None
    route=[]
    node=destination

    while node!=start:
        route.append(node)
        neighbors=graph[node]
        min_distance=float('inf')
        next_node=None
        for neighbor, weight in neighbors.items():
            if distances[neighbor]+weight==distances[node] and distances[neighbor]<min_distance:
                min_distance=distances[neighbor]
                next_node=neighbor
        if next_node is None or next_node in route:
            return None
        node=next_node
    route.append(start)
    route.reverse()
    return route
#Example usage 
#graph={
#    'A':{'B':3, 'C':99, 'D':7, 'E':99},
#   'B':{'A':3, 'C':4, 'D':2, 'E':99},
#  'C':{'B':3, 'C':99, 'D':7, 'E':99},
#    'D':{'A':7, 'B':2, 'C':5, 'E':4},
#    'E':{'A':99, 'B':99, 'C':6, 'D':4}
#}
graph={}
num_nodes=int(input("enter the number of nodes in graph:"))
for i in range(num_nodes):
    node=input(f"enter node {i+1}:")
    neighbors={}
    num_neighbors=int(input(f"Enter the neighbors for node {node}: "))
    for j in range(num_neighbors):
        neighbor, weight=input(f"enter the neighbor {j+1} and its weight").split()
        neighbors[neighbor]=int(weight)
    graph[node]=neighbors    


'''
enter the number of nodes in graph:5
enter node 1:A
Enter the neighbors for node A: 4
enter the neighbor 1 and its weightB 3
enter the neighbor 2 and its weightC 99
enter the neighbor 3 and its weightD 7
enter the neighbor 4 and its weightE 99
enter node 2:B
Enter the neighbors for node B: 4
enter the neighbor 1 and its weightA 3
enter the neighbor 2 and its weightC 4
enter the neighbor 3 and its weightD 2
enter the neighbor 4 and its weightE 99
enter node 3:C
Enter the neighbors for node C: 4
enter the neighbor 1 and its weightA 99
enter the neighbor 2 and its weightB 4
enter the neighbor 3 and its weightD 5
enter the neighbor 4 and its weightE 6
enter node 4:D
Enter the neighbors for node D: 4
enter the neighbor 1 and its weightA 7
enter the neighbor 2 and its weightB 2
enter the neighbor 3 and its weightC 5
enter the neighbor 4 and its weightE 4
enter node 5:E
Enter the neighbors for node E: 4
enter the neighbor 1 and its weightA 99
enter the neighbor 2 and its weightB 99
enter the neighbor 3 and its weightC 6
enter the neighbor 4 and its weightD 4
enter the start location:A
enter the destination location:E
Optimal route:  A->B->D->E
'''


start_location=input("enter the start location:")
destination_location=input("enter the destination location:")
optimal_route=find_optimal_route(graph,start_location,destination_location)
if optimal_route is None:
    print("No valid route")
else:
    print("Optimal route: ",'->'.join(optimal_route))

