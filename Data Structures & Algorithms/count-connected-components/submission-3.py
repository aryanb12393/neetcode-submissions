from collections import deque

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # print(graph)

        visited = set()
        final_num = 0

        def bfs(node):

            visited.add(node)

            queue = deque([node])

            while queue:
                
                curr_node = queue.popleft()

                curr_nei = graph[curr_node]

                for nei in curr_nei:

                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            

        for i in range(n):
            if i not in visited:
                bfs(i)
                final_num += 1


        return final_num

        # 0 : [1]
        # 1: [0, 2]
        # 2: [1]

        # 0
            # 1
