from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0
        
        stops_to_buses = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stops_to_buses[stop].add(i)
        
        visited_stops = set()
        visited_buses = set()
        queue = deque([(source, 0)])  # (stop, buses taken)
        while queue:
            stop, buses_taken = queue.popleft()
            if stop == target:
                return buses_taken
            for bus_i in stops_to_buses[stop]:
                if bus_i not in visited_buses:
                    visited_buses.add(bus_i)
                    for next_stop in routes[bus_i]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, buses_taken + 1))
        return -1