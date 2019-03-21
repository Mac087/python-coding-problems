# In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.

# Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.

# The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.

# For example, the following input graph:

# ABACA
# [(0, 1),
#  (0, 2),
#  (2, 3),
#  (3, 4)]
# Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).

# The following input graph:

# A
# [(0, 0)]
# Should return null, since we have an infinite loop.

VISITED = 0
UNVISITED = 1
VISITING = 2

def max_path(s, lst):
    adj = [[] for v in s]
    # Build adjacency list
    for u, v in lst:
        adj[u].append(v)

    # Create matrix cache
    dp = [[0 for _ in range(26)] for _ in range(len(s))]
    state = {v: UNVISITED for v in range(len(s))}

    def dfs(v):
        state[v] = VISITING
        for neighbour in adj[v]:
            if state[neighbour] == VISITING:
                # We have a cycle
                return True
            dfs(neighbour)
            for i in range(26):
                dp[v][i] = dp[neighbour][i]
        current_char = ord(s[v]) - ord('A')
        dp[v][current_char] += 1
        state[v] = VISITED

    # Run DFS on graph
    for v in range(len(s)):
        if state[v] == UNVISITED:
            has_cycle = dfs(v)
            if has_cycle:
                return None

    return max(max(v for v in node) for node in dp)