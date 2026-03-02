import collections

# =============================================================================
# BREADTH-FIRST SEARCH (BFS) EXPLAINER & VISUALIZER
# =============================================================================
# This project demonstrates how BFS explores a graph level by level.
# It uses a Queue (First-In-First-Out) to track which nodes to visit next.
# =============================================================================

def bfs_with_visualization(graph, start_node):
    """
    Performs BFS on a graph and prints a step-by-step visualization.
    
    Args:
        graph (dict): Adjacency list representation of the graph.
        start_node: The node where the search begins.
    """
    
    # 1. INITIALIZATION
    # We use a deque (double-ended queue) for O(1) pop performance from the left.
    queue = collections.deque([start_node])
    
    # We use a set for 'visited' to ensure O(1) lookup time.
    visited = {start_node}
    
    # This list keeps track of the order in which nodes are fully processed.
    traversal_path = []
    
    step = 1
    print(f"\n--- BFS STARTING AT NODE: {start_node} ---")

    # 2. THE CORE LOOP
    # While there are still nodes in the queue, the search continues.
    while queue:
        # VISUALIZATION: Show current state of the Queue
        print(f"\nStep {step}:")
        print(f"  Current Queue: {list(queue)}")
        
        # Dequeue the first node added (FIFO - First In, First Out)
        current_node = queue.popleft()
        traversal_path.append(current_node)
        
        print(f"  Processing node: [ {current_node} ]")

        # 3. EXPLORE NEIGHBORS
        # Look at every node connected to the current node.
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                # If neighbor hasn't been visited, mark it and add to queue.
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"    -> Found new neighbor: {neighbor} (Added to Queue)")
            else:
                print(f"    -> Neighbor {neighbor} already visited. Skipping.")
        
        step += 1

    # 4. FINAL RESULTS
    print("\n" + "="*40)
    print(f"BFS COMPLETE")
    print(f"Final Traversal Order: {' -> '.join(map(str, traversal_path))}")
    print("="*40 + "\n")


# =============================================================================
# EXAMPLE 1: SIMPLE DIRECTED GRAPH
# =============================================================================
# Visualization of the Structure:
#     A ----> B ----> D
#     |       |
#     v       v
#     C ----> E
# =============================================================================

simple_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': [],
    'E': []
}

# =============================================================================
# EXAMPLE 2: A SOCIAL NETWORK (Undirected)
# =============================================================================
# Shows "degrees of separation". BFS is perfect for finding the shortest path
# in an unweighted social graph (finding "Friends of Friends").
# =============================================================================

social_network = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'David', 'Eve'],
    'Charlie': ['Alice', 'Eve'],
    'David': ['Bob'],
    'Eve': ['Bob', 'Charlie']
}


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Illustration of the Logic
    print("CONCEPTUAL ILLUSTRATION:")
    print("BFS works like a ripple in a pond.")
    print("Level 0: Start Node")
    print("Level 1: All immediate neighbors")
    print("Level 2: Neighbors of neighbors (that weren't in Level 1)")
    
    # Run Example 1
    print("\nRUNNING EXAMPLE 1: Simple Graph")
    bfs_with_visualization(simple_graph, 'A')
    
    # Run Example 2
    print("\nRUNNING EXAMPLE 2: Social Network")
    # Note: In undirected graphs, BFS handles cycles automatically via the 'visited' set.
    bfs_with_visualization(social_network, 'Alice')

# =============================================================================
# SUMMARY OF BFS PROPERTIES:
# 1. Space Complexity: O(V) where V is the number of vertices (for queue/visited).
# 2. Time Complexity: O(V + E) where E is the number of edges.
# 3. Shortest Path: BFS is guaranteed to find the shortest path from a start node 
#    to any other node in an UNWEIGHTED graph.
# =============================================================================