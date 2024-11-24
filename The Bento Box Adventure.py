def find_friday_restaurant(a, b, c, d):
    # Create a set of all restaurant numbers from 1 to 5
    all_restaurants = {1, 2, 3, 4, 5}
    
    # Create a set of visited restaurants
    visited_set = {a, b, c, d}
    
    # Find the remaining restaurant
    remaining_restaurants = all_restaurants - visited_set
    
    # Return the only remaining restaurant
    return remaining_restaurants.pop()

# Input: Four integers representing the visited restaurants
a, b, c, d = map(int, input().split())

# Output: The restaurant to visit on Friday
print(find_friday_restaurant(a, b, c, d))
