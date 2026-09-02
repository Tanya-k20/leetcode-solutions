class Solution:
    def containVirus(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(i, j, visited):
            if not (0 <= i < m and 0 <= j < n) or (i, j) in visited:
                return set(), 0
            if mat[i][j] == 2:
                return set(), 0
            elif mat[i][j] == 0:
                return {(i, j)}, 1
            
            visited.add((i, j))
            infected, walls = set(), 0
            for dx, dy in DIRECTIONS:
                ni, nj = i + dx, j + dy
                next_infected, next_walls = dfs(ni, nj, visited)
                infected |= next_infected
                walls += next_walls
            return infected, walls
        
        def quarantine(i, j):
            if 0 <= i < m and 0 <= j < n and mat[i][j] == 1:
                mat[i][j] = 2
                for dx, dy in DIRECTIONS:
                    quarantine(i + dx, j + dy)
        
        ans = 0
        while True:
            visited, regions = set(), []
            for i in range(m):
                for j in range(n):
                    if mat[i][j] == 1 and (i, j) not in visited:
                        infected, walls = dfs(i, j, visited)
                        if infected:
                            regions.append((infected, walls, (i, j)))
            
            if not regions:
                break
            
            regions.sort(key=lambda x: (-len(x[0]), x[1]))
            max_infected, max_walls, start = regions[0]
            ans += max_walls
            quarantine(*start)
            
            for region in regions[1:]:
                for i, j in region[0]:
                    mat[i][j] = 1
        
        return ans