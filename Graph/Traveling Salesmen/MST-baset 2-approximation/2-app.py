import sys
import heapq
from typing import Dict, List, Tuple

def mst_prim(G: Dict[int, Dict[int, float]], w: Dict[Tuple[int, int], float], r: int) -> Dict[int, int]:
    Q = list(G.keys())
    key = {u: sys.maxsize for u in Q}
    pi = {u: None for u in Q}
    key[r] = 0
    # EXTRACT-MIN
    heap = [(key[u], u) for u in Q]
    heapq.heapify(heap)
    while heap:
        _, u = heapq.heappop(heap)
        if u not in Q:
            continue
        Q.remove(u)
        for v in G[u]:
            if v in Q and w.get((u, v), sys.maxsize) < key[v]:
                pi[v] = u
                key[v] = w[(u, v)]
                heapq.heappush(heap, (key[v], v))
    return pi

def build_mst_adjacency(pi: Dict[int, int]) -> Dict[int, List[int]]:
    mst = {u: [] for u in pi}
    for v, u in pi.items():
        if u is not None:
            mst[u].append(v)
    return mst

def preorder_traversal(mst: Dict[int, List[int]], root: int) -> List[int]:
    result = []
    stack = [root]
    
    while stack:
        u = stack.pop()
        result.append(u)
        for v in reversed(mst[u]):
            stack.append(v)
    
    return result

def approx_tsp_tour(G: Dict[int, Dict[int, float]], w: Dict[Tuple[int, int], float]) -> List[int]:
    r = next(iter(G.keys()))
    pi = mst_prim(G, w, r)

    mst_adj = build_mst_adjacency(pi)
    
    L = preorder_traversal(mst_adj, r)
    
    return L + [r]

if __name__ == "__main__":
    G = {
        0: {1, 2, 3},
        1: {0, 2, 3},
        2: {0, 1, 3},
        3: {0, 1, 2}
    }
    
    w = {
        (0, 1): 2, (1, 0): 2,
        (0, 2): 3, (2, 0): 3,
        (0, 3): 9, (3, 0): 9,
        (1, 2): 4, (2, 1): 4,
        (1, 3): 8, (3, 1): 8,
        (2, 3): 7, (3, 2): 7
    }
    
    tour = approx_tsp_tour(G, w)
    print("Przybliżony cykl TSP:", tour)
    
    cost = sum(w[(tour[i], tour[i+1])] for i in range(len(tour)-1))
    print("Koszt cyklu:", cost)