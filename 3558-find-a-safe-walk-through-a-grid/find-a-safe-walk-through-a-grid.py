from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        # min_loss[r][c] stores the minimum health lost to reach (r, c)
        min_loss = [[float('inf')] * n for _ in range(m)]
        
        q = deque([(0, 0)])
        min_loss[0][0] = grid[0][0]
        
        while q:
            r, c = q.popleft()
            
            if r == m - 1 and c == n - 1:
                return health - min_loss[r][c] >= 1
                
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_loss = min_loss[r][c] + grid[nr][nc]
                    if next_loss < min_loss[nr][nc]:
                        min_loss[nr][nc] = next_loss
                        # 0-1 BFS optimization: 0 cost to front, 1 cost to back
                        if grid[nr][nc] == 0:
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))
                            
        return False