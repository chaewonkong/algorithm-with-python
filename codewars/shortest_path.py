"""Path Finder #2: shortest path

You are at position [0, 0] in maze NxN and you can only move in
one of the four cardinal directions (i.e. North, East, South, West). 
Return the minimal number of steps to exit position [N-1, N-1] 
if it is possible to reach the exit from the starting position. 
Otherwise, return false in JavaScript/Python.

Empty positions are marked .. 
Walls are marked W. 
Start and exit positions are guaranteed to be empty in all test cases.
"""


# Tell variables and constants by the cases they're written.
# D and WALL will never change: they're constants.
D = [(0, 1), (0, -1), (1, 0), (-1, 0)]
WALL = 'W'

# Very simple BFS problem
def path_finder(maze):
    maze = maze.split()
    N = len(maze)
    DEST = (N-1, N-1) # Dest won't change in this problem
    distances = [[-1] * N for _ in range(N)]
    distances[0][0] = 0
    queue = [(0, 0)]
    
    while queue:
        r, c = queue.pop(0)
        for dr, dc in D:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < N and 0 <= new_c < N \
                and distances[new_r][new_c] == -1 \
                and maze[new_r][new_c] != WALL:
                distances[new_r][new_c] = distances[r][c] + 1
                # If we have reached DEST, just return it. No need to move on.
                if (new_r, new_c) == DEST:
                    return distances[new_r][new_c]
                queue.append((new_r, new_c))
                
    # If we couldn't reach DEST, return False
    return False

'''
def path_finder(s):
    maze = [[1 if p == "." else 0 for p in line] for line in s.split("\n")]
    N = len(maze)
    adj = [[] for _ in range(N*N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j]:
                target = adj[i+j+(N-1)*i]
                if i > 0 and maze[i-1][j] == 1:
                    target.append(i-1+j+(N-1)*(i-1))
                if j > 0 and maze[i][j-1] == 1:
                    target.append(i+j-1+(N-1)*i)
                if i < N-1 and maze[i+1][j] == 1:
                    target.append(i+1+j+(N-1)*(i+1))
                if j < N-1 and maze[i][j+1] == 1:
                    target.append(i+j+1+(N-1)*i)

    def bfs(adj, start, end):
        N = len(adj)
        distance = [-1] * N
        parent = [-1] * N
        queue = []
        distance[start] = 0
        parent[start] = start
        queue.append(start)
        while queue:
            here = queue.pop(0)
            for i in range(len(adj[here])):
                there = adj[here][i]
                if distance[there] == -1:
                    queue.append(there)
                    distance[there] = distance[here] + 1
                    parent[there] = here
        path = [end]
        while parent[end] != end:
            end = parent[end]
            if end >= 0:
                path.append(end)
            path.reverse()
        return path
    
    path = bfs(adj, 0, len(adj)-1)
    return len(path)-1 if len(path) > 1 else False
'''  
    


a = "\n".join([
  ".W.",
  ".W.",
  "..."
])

b = "\n".join([
  ".W.",
  ".W.",
  "W.."
])

c = "\n".join([
  "......",
  "......",
  "......",
  "......",
  "......",
  "......"
])

d = "\n".join([
  "......",
  "......",
  "......",
  "......",
  ".....W",
  "....W."
])

def assert_equals(f, ret):
    if f == ret:
        print(True)
    else:
        print(False)

assert_equals(path_finder(a), 4)
assert_equals(path_finder(b), False)
assert_equals(path_finder(c), 10)
assert_equals(path_finder(d), False)
