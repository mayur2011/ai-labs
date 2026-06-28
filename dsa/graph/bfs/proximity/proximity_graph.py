from collections import deque

def find_bda_complex(graph, start, target):
    # Queue stores tuple of (current_location, path_taken_so_far)
    queue = deque([(start, [start])])
    visited = set([start])
    
    print(f"Entering the local street grid at: {start}")
    
    while queue:
        current_node, path = queue.popleft()
        
        # If we reached the BDA complex, we are done!
        if current_node == target:
            print(f"Destination Reached! Path taken: {' -> '.join(path)}")
            return True
            
        print(f"Currently at [{current_node}]. Evaluating its local neighbors...")
        
        # Check all directly connected local streets
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
                
    print("Destination could not be reached via local streets.")
    return False

# The HSR Layout Proximity Graph (Adjacency List)
hsr_street_network = {
    'Silk Board Gateway': ['HSR 14th Main Road', 'Sector 3 Junction'],
    'HSR 14th Main Road': ['Silk Board Gateway', 'HSR 27th Main Road', 'HSR BDA Complex'],
    'Sector 3 Junction': ['Silk Board Gateway', 'Sector 5 Lane'],
    'HSR 27th Main Road': ['HSR 14th Main Road', 'HSR BDA Complex'],
    'Sector 5 Lane': ['Sector 3 Junction'],
    'HSR BDA Complex': ['HSR 14th Main Road', 'HSR 27th Main Road'] # Target
}

# Run the local search
find_bda_complex(hsr_street_network, start='Silk Board Gateway', target='HSR BDA Complex')