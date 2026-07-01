from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        
        # 1. Multi-source BFS to calculate minimum distance to any thief
        dist = [[float('inf')] * n for _ in range(n)]
        q = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((0, r, c))
                    
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while q:
            d, r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float('inf'):
                    dist[nr][nc] = d + 1
                    q.append((d + 1, nr, nc))
                    
        # 2. Max-Heap (Dijkstra) to find the path maximizing the safeness factor
        # Python's heapq is a min-heap, so we store negative safeness values
        max_heap = [(-dist[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True
        
        while max_heap:
            sf, r, c = heapq.heappop(max_heap)
            sf = -sf  # Convert back to positive
            
            if r == n - 1 and c == n - 1:
                return sf
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    # The safeness of the next cell is limited by the current path's safeness
                    heapq.heappush(max_heap, (-min(sf, dist[nr][nc]), nr, nc))
                    
        return 0