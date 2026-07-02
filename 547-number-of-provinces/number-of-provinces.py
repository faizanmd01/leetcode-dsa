class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(start: int):
            for neighbor, connected in enumerate(isConnected[start]):
                if connected and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                provinces += 1
                
        return provinces