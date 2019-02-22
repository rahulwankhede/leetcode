class Solution:
    def maxIncreaseKeepingSkyline(self, grid: 'List[List[int]]') -> 'int':
        n = len(grid)
        top = [0]*n
        left = [0]*n
        for i in range(n):
            top[i] = max(grid[j][i] for j in range(n))
            left[i] = max(grid[i][j] for j in range(n))
        count = 0
        for i in range(n):
            for j in range(n):
                count += min(top[i], left[j]) - grid[i][j]
        return count