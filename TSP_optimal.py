import networkx as nx 
def get_distances(num_nodes):
  distances={}
  for i in range(1,num_nodes+1):
    for j in range(i+1,num_nodes+1):
      distance=float(input(f"enter the distance between the node{i} and node{j} :"))
      distances[(i,j)]=distance
      distances[(j,i)]=distance
  return distances
def tsp_optimal_drilling(distances):
  G=nx.Graph()
  G.add_weighted_edges_from((i,j,distance)for(i,j),distance in distances.items())
  optimal_order=nx.approximation.traveling_salesman_problem(G,cycle=True)
  return optimal_order
def calculate_optimal_cost(drill_order,distances):
  total_cost=sum(distances[(drill_order[i],drill_order[i+1])]for i in range(len(drill_order)-1))
  return total_cost
if __name__ == "__main__":
  while True:
    num_nodes=int(input("enter the number of drill holes (nodes): "))
    distances=get_distances(num_nodes)
    optimal_order=tsp_optimal_drilling(distances)
    optimal_cost=calculate_optimal_cost(optimal_order, distances)
    print("Optimal drilling order : ",optimal_order)
    print("Total Optimal cost : ",optimal_cost)
    try_again=input("Do you want to try again with a different number of nodes?yes/No").lower()
    if try_again!="yes":
                    break