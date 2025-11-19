"""
LEETCODE 994 (Medium)

You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        if rows == 0:
            return -1
        cols = len(grid[0])
        
        rotten = deque()
        fresh_count = 0
        time = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1
                    
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while rotten and fresh_count > 0:
            for _ in range(len(rotten)):
                x, y = rotten.popleft()
                
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy
                    
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        fresh_count -= 1
                        rotten.append((new_x, new_y))
            time += 1
            
        if fresh_count == 0:
            return time
        else:
            return -1
        

if __name__ == "__main__":
    solution = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(solution.orangesRotting(grid))