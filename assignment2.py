def find_travel_route(start_city, tickets, visited_cities):
    from collections import defaultdict, deque

    # Step 1: Build the graph
    graph = defaultdict(list)
    for from_city, to_city in tickets:
        graph[from_city].append(to_city)
    
    # Ensure we have all cities in the graph
    for city in visited_cities:
        if city not in graph:
            graph[city] = []
    
    # Step 2: Perform DFS to find the route
    route = []
    visited_set = set()
    
    def dfs(city):
        if city in visited_set:
            return
        visited_set.add(city)
        route.append(city)
        for neighbor in sorted(graph[city]):
            if neighbor not in visited_set:
                dfs(neighbor)
    
    # Start DFS from the start city
    dfs(start_city)
    
    # Ensure the route contains all visited cities
    if set(route) == set(visited_cities):
        return route
    else:
        return "Error: The route does not match the visited cities."

# Example input
start_city = 'Kiev'
tickets = [('Kiev', 'Prague'), ('Prague', 'Zurich'), ('Zurich', 'Amsterdam'),
           ('Amsterdam', 'Barcelona'), ('Barcelona', 'Berlin'), ('Berlin', 'Kiev')]
visited_cities = ['Kiev', 'Prague', 'Zurich', 'Amsterdam', 'Barcelona', 'Berlin']

# Find and print the travel route
route = find_travel_route(start_city, tickets, visited_cities)
print(route)
