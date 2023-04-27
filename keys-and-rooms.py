class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict()
        for i,j in enumerate(rooms):
            graph[i] = j

        queue = deque([0])
        visited = set([0])
        
        while queue:
            node = queue.popleft()
            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
         
        count = len(rooms)       
        if count==len(visited):
            return True
        return False