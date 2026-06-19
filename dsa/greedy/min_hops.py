def min_hops_to_hsr(milestones) -> int:
    # If there's only 1 milestone, we are already at HSR BDA Complex
    if len(milestones) <= 1:
        return 0
    
    hops = 0
    current_max_reach = 0
    furthest_next_step = 0
    
    # Iterate through the hubs (we don't need to process the last destination node)
    for i in range(len(milestones) - 1):
        # Update the absolute furthest milestone we can eventually touch
        furthest_next_step = max(furthest_next_step, i + milestones[i])
        
        # If we have reached the limit of our current hop's momentum
        if i == current_max_reach:
            hops += 1  # We must make a greedy jump
            current_max_reach = furthest_next_step
            
            # If our new reach touches or exceeds HSR BDA Complex, we break early
            if current_max_reach >= len(milestones) - 1:
                break
                
    return hops

# Example Walkthrough:
# Index:       [  0,   1,   2,   3,   4,   5]
# Milestone:   [  2,   3,   1,   1,   4,   0]
# Location:   [Ragigudda, BTM, AXA, SilkBoard, HSR14th, HSR_BDA]

route = [2, 3, 1, 1, 4, 0]
print(f"Minimum jumps required: {min_hops_to_hsr(route)}")  # Output: 2