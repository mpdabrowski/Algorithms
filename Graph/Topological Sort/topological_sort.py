def topological_sort(G):
    def DFS_topo(G, s):
        nonlocal curLabel
        visited[s] = True
        for v in G[s]:
            if False == visited[v]:
                DFS_topo(G, v)
        f[s] = curLabel
        curLabel -= 1
    
    visited = {v: False for v in G}
    curLabel = len(G)
    f = {}
    for v in G:
        if False == visited[v]:
            DFS_topo(G, v)
    
    return sorted(f, key=lambda x: f[x])

G = {
    's': ['v', 'w'],
    'v': ['t'],
    'w': ['t'],
    't': []
}


print(topological_sort(G))