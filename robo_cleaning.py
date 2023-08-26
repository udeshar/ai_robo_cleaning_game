from queue import PriorityQueue
from queue import Queue

def is_valid(row, col, rows, cols, grid):
    return 0 <= row < rows and 0 <= col < cols and grid[row][col] != 'X'

def bfs_cleaning(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    position = (0, 0)
    
    visited = set()
    queue = Queue()
    queue.put(position)
    
    while not queue.empty():
        row, col = queue.get()
        if (row, col) in visited:
            continue
        
        visited.add((row, col))
        print(f"Cleaning tile at ({row}, {col})")
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col, rows, cols, grid):
                queue.put((new_row, new_col))

def dfs_cleaning(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    position = (0, 0)
    
    visited = set()
    stack = [position]
    
    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        
        visited.add((row, col))
        print(f"Cleaning tile at ({row}, {col})")
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col, rows, cols, grid):
                stack.append((new_row, new_col))

def a_star_cleaning(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    start = (0, 0)
    goal = (rows - 1, cols - 1)
    
    def heuristic(node):
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])
    
    visited = set()
    open_list = PriorityQueue()
    open_list.put((0, start))
    
    while not open_list.empty():
        cost, (row, col) = open_list.get()
        if (row, col) in visited:
            continue
        
        visited.add((row, col))
        print(f"Cleaning tile at ({row}, {col})")
        
        if (row, col) == goal:
            break
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid(new_row, new_col, rows, cols, grid):
                new_cost = cost + 1 + heuristic((new_row, new_col))
                open_list.put((new_cost, (new_row, new_col)))

def hill_climbing_cleaning(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    current_node = (0, 0)
    
    def heuristic(node):
        return abs(node[0] - (rows - 1)) + abs(node[1] - (cols - 1))
    
    while True:
        neighbors = []
        
        for dr, dc in directions:
            new_row, new_col = current_node[0] + dr, current_node[1] + dc
            if is_valid(new_row, new_col, rows, cols, grid):
                neighbors.append((new_row, new_col))
        
        best_neighbor = min(neighbors, key=lambda n: heuristic(n))
        
        if heuristic(best_neighbor) >= heuristic(current_node):
            break
        
        print(f"Cleaning tile at {best_neighbor}")
        current_node = best_neighbor

# Example grid layout (replace it with your own):
grid = [
    ['0', '0', 'X', '0', 'X'],
    ['0', 'X', '0', '0', '0'],
    ['0', '0', '0', 'X', '0'],
    ['X', '0', 'X', '0', '0'],
    ['0', '0', '0', '0', 'X']
]

print("Original grid:")
for row in grid:
    print(" ".join(row))

print("\nStarting BFS cleaning:")
bfs_cleaning(grid)

print("\nStarting DFS cleaning:")
dfs_cleaning(grid)

# Call A* cleaning
print("\nStarting A* cleaning:")
a_star_cleaning(grid)

# Call Hill Climbing cleaning
print("\nStarting Hill Climbing cleaning:")
hill_climbing_cleaning(grid)

print("\nGrid after cleaning:")
for row in grid:
    print(" ".join(row))
