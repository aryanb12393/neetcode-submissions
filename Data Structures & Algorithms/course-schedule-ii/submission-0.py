class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        def construct_graph(pre_list):
            
            graph = {}

            for pair in pre_list:
                
                curr = pair[0]
                pre = pair[1]

                if pre not in graph:
                    graph[pre] = [curr]
                else:
                    graph[pre].append(curr)

            return graph
        
        def find_indegree_initial(graph):

            indegree = [0] * numCourses

            for _, vertices in graph.items():

                for vertex in vertices:
                    
                    # print(vertex)
                    indegree[vertex] += 1
            
            return indegree
   
        def top_sort(graph, indegree):
            
            queue = deque()

            for idx, val in enumerate(indegree):
                if val == 0:
                    queue.append(idx)
            
            top_sort = []

            while queue:

                node = queue.popleft()
                top_sort.append(node)
                neis = graph.get(node)

                if neis is not None:

                    for nei in neis:
                        
                        indegree[nei] -= 1

                        if indegree[nei] == 0:
                            queue.append(nei)

            return top_sort

        graph = construct_graph(prerequisites)
        initial_indegree = find_indegree_initial(graph)
        res = top_sort(graph, initial_indegree)
        
        if len(res) == numCourses:
            return res

        return []