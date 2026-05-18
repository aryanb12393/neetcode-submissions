class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    
        adjacency_list = {}
        
        for ticket in tickets:

            stop_one = ticket[0]
            stop_two = ticket[1]

            if stop_one not in adjacency_list:
                adjacency_list[stop_one] = [stop_two]
            else:
                adjacency_list[stop_one].append(stop_two)

        for key in adjacency_list.keys():

            curr_list = adjacency_list[key]
            curr_list = sorted(curr_list)
            adjacency_list[key] = curr_list[::-1]
        
        print(adjacency_list)
        master_list = []

        def dfs(node):

            neighbours = adjacency_list.get(node)

            # if not neighbours:
            #     master_list.append(node)
            #     return

            while neighbours:

                curr_neighbour = neighbours.pop()
                dfs(curr_neighbour)
            
            master_list.append(node)

        dfs("JFK")

        return (master_list[::-1])

                


