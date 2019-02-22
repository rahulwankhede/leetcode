def maxIncreaseKeepingSkyline(grid: 'List[List[int]]') -> 'int':
    top = [max(row) for row in grid]
    left = [max(col) for col in zip(*grid)]
        
    return sum((min(top[c], left[r]) - val)
            for r, row in enumerate(grid)
            for c, val in enumerate(row)
            )

"""testing"""

grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
print(maxIncreaseKeepingSkyline(grid))
