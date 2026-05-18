class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # print(graph)

        visited = set()
        final_num = 0

        def dfs(node):
            
            visited.add(node)

            curr_nei = graph[node]

            for nei in curr_nei:
                if nei not in visited:
                    dfs(nei) 
            
        for i in range(n):
            if i not in visited:
                dfs(i)
                final_num += 1


        return final_num

        # 0 : [1]
        # 1: [0, 2]
        # 2: [1]

        # 0
            # 1
