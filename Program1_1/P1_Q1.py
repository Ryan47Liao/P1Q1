'''
Created on Apr 1, 2021

#Submitter: bliao2 (Liao, Bowen)
#Partner: boiv (Vo, Boi Loc) 
We certify that we worked cooperatively on this programming assignment, 
according to the rules for pair programming 
'''
import prompt
def read_graph(file)->dict:
    "This function takes in an opened file of graph and outputs a dictionary. "
    Dict = {}
    for line in file:
        line = line.rstrip('\n')
        if line.split(";")[0] in Dict:
            Dict[line.split(";")[0]].append(line.split(";")[1])
        else:
            Dict[line.split(";")[0]] = list(line.split(";")[1])
    return Dict
    
def graph_as_str(graph:dict)->str:
    """
    This function takes in a dictionary of a graph and returns a multi-line string 
    that is sorted by the keys of the dictionary. And the items of the dictionary is 
    also sorted. 
    """
    STR = ""
    for node in sorted(list(graph.items())):
        STR += node[0] + "->" + str(sorted(node[1])) + "\n"
    print(STR)
    return STR
    
def reachable(Graph:dict,start:str,tracing:bool = False):
    """
    This function takes in a dictionary of the graph and a starting point, 
    it will output all the nodes that is reachable in the graph from the starting point.
    When tracing is enabled (True), it will also print all the procedue.
    """
    reached = set()
    exploreing = list(start)
    while len(exploreing) > 0:
        if tracing:
            print(f"reached set  = {reached}\nexploring set = {exploreing}",end='')
        node = exploreing[0]
        for j in ([] if Graph.get(node) is None else Graph.get(node)):
            if j not in reached and j not in exploreing:
                exploreing.append(j)
        reached.add(exploreing.pop(0))
        if tracing:
            print(
                f"""
transfering node {node} from exploring set to the reached set
after adding all nodes reachable directly from {node} but not already in reached,exploring = {exploreing}
                """)
    return reached

#User Prompt 
def UI():
    "An prompt based User Interface"
    file = None
    while file is None:
        try:
            file = open(input("Input the file name detailing the graph:"))
            Graph = read_graph(file)
        except FileNotFoundError:
            print("Error, file not found...")
    
    print("Graph: str (source node) -> [str] (sorted destination nodes)")
    graph_as_str(Graph)
    while True:
        start = prompt.for_string(' Input one starting node (or input done)', 
                                   is_legal = lambda start: start in Graph or start == 'done'
                                   ,error_message= "Illegal: not a source node")
        if start == "done":
            return 
        tracing = prompt.for_bool("Input tracing algorithm option", True, "Enter False to disable tracing")
        print(f"From the starting node {start}, its reachable nodes are:",reachable(Graph,start,tracing))
        
if __name__ == "__main__":
    UI()
    
    
#Write a script at the bottom of this module (in if __name__ == '__main__':) that prompts the user to enter the file storing the graph and start node (rejecting any string that is not a source node in the graph) or the word done; calls these functions with the entered information to solve the problem, and print the appropriate information: the graph and the set containing all the node labels (body is 9 lines).