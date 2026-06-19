places = {
    0: "Ragigudda",
    10: "BTM Layout",
    20: "Silk Board Metro Station",
    30: "Central Silk Board",
    40: "HSR 14th Main",
    50: "HSR XYZ Signal",
    55: "HSR BDA Complex",
    60: "Agara"
}

def skip_list_search(network, target) -> bool:
    express_layer = network[0]
    local_layer = network[1]
    
    # Step 1: Search on the Express Layer (Flyover)
    express_idx = 0
    print(f"Starting on Express Layer... From {places[express_layer[0]]}")
    
    while express_idx + 1 < len(express_layer) and express_layer[express_idx + 1] <= target:
        express_idx += 1
        print(f"-> Zooming on Flyover to Major Hub: {places[express_layer[express_idx]]}")
        
    # Find where the flyover aligned us on the local street level
    current_val = express_layer[express_idx]
    local_idx = local_layer.index(current_val)
    
    print(f"\n Dropped down to Local Layer at stop...")
    
    # Step 2: Search on the Local Layer (Street Level)
    while local_idx < len(local_layer):
        print(f"-> Checking local street stop: {places[local_layer[local_idx]]}")
        if local_layer[local_idx] == target:
            return True  # Found HSR Complex!
        if local_layer[local_idx] > target:
            break  # Overshot the target; it doesn't exist
        local_idx += 1
        
    return False

# Example Drive:
# Target: 55 (HSR BDA Complex)
transit_network = [
    [0, 30, 60],          # Express Layer (Major Hubs)
    [0, 10, 20, 30, 40, 50, 55, 60]  # Local Layer (All Stops)
]

found = skip_list_search(transit_network, target=55)
print(f"Destination Found: {found}")