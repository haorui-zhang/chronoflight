from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from datetime import datetime, timedelta
import math
from collections import defaultdict, deque
import json
from flight_data import AIRPORTS, FLIGHTS

app = Flask(__name__)
CORS(app)

def build_flight_network():
    """Build a graph representation of the flight network."""
    network = defaultdict(list)
    for flight in FLIGHTS:
        network[flight["from"]].append(flight)
        # Add reverse connections for better pathfinding
        network[flight["to"]].append({
            "from": flight["to"],
            "to": flight["from"],
            "departure": flight["arrival"],
            "arrival": flight["departure"],
            "flying_hours": flight["flying_hours"]
        })
    return network

def find_reachable_destinations(start_airport, max_hours):
    """Find all reachable destinations within max_hours using BFS."""
    network = build_flight_network()
    visited = {}  # Dictionary to track best times for each airport
    reachable = []
    queue = deque([(start_airport, 0, [])])  # (airport, current_time, path)
    
    # First pass: find direct connections
    direct_connections = set()
    for flight in network[start_airport]:
        direct_connections.add(flight["to"])
    
    while queue:
        current, current_time, path = queue.popleft()
        
        # Skip if we've found a better path to this airport
        if current in visited and visited[current] <= current_time:
            continue
            
        visited[current] = current_time
        
        # Add current airport to reachable destinations if it's not the start
        if current != start_airport:
            airport_info = AIRPORTS[current]
            reachable.append({
                'airport': current,
                'city': airport_info['city'],
                'coordinates': airport_info['coordinates'],
                'flying_hours': current_time,
                'hops': len(path),
                'path_details': path.copy(),
                'is_direct': current in direct_connections
            })
        
        # Explore all possible flights from current airport
        for flight in network[current]:
            next_airport = flight['to']
            flight_time = flight['flying_hours']
            total_time = current_time + flight_time
            
            # Skip if this path would exceed max hours
            if total_time > max_hours:
                continue
                
            # Create new path with this flight
            new_path = path + [{
                'from': {
                    'airport': current,
                    'time': flight['departure']
                },
                'to': {
                    'airport': next_airport,
                    'time': flight['arrival']
                },
                'flying_hours': flight_time
            }]
            
            # Add to queue if we haven't found a better path to this airport
            if next_airport not in visited or visited[next_airport] > total_time:
                queue.append((next_airport, total_time, new_path))
    
    # Sort reachable destinations by flying hours
    reachable.sort(key=lambda x: x['flying_hours'])
    
    # Ensure we have a good mix of direct and connecting flights
    direct_flights = [d for d in reachable if d['is_direct']]
    connecting_flights = [d for d in reachable if not d['is_direct']]
    
    # Prioritize direct flights for nearby destinations
    result = []
    for dest in reachable:
        if dest['is_direct'] and dest['flying_hours'] <= 8:
            result.append(dest)
        elif not dest['is_direct'] and dest['flying_hours'] > 8:
            result.append(dest)
    
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/airports')
def get_airports():
    return jsonify(AIRPORTS)

@app.route('/api/reachable')
def get_reachable():
    hours = float(request.args.get('hours', 0))
    departure = request.args.get('departure', 'JFK')
    
    if departure not in AIRPORTS:
        return jsonify({'error': 'Invalid departure airport'}), 400
    
    start_airport = AIRPORTS[departure]
    reachable = find_reachable_destinations(departure, hours)
    
    # Debug print to verify paths
    print(f"\nDebug: Checking paths from {departure} for {hours} hours:")
    print(f"Total reachable destinations: {len(reachable)}")
    direct_flights = [d for d in reachable if d['is_direct']]
    print(f"Direct flights: {len(direct_flights)}")
    connecting_flights = [d for d in reachable if not d['is_direct']]
    print(f"Connecting flights: {len(connecting_flights)}")
    
    return jsonify({
        "start": {
            "airport": departure,
            "city": start_airport['city'],
            "coordinates": start_airport['coordinates']
        },
        "reachable": reachable,
        "airports": AIRPORTS
    })

@app.route('/api/test-path')
def test_path():
    # Test with 48 hours to ensure we can reach SIN
    reachable = find_reachable_destinations("JFK", 48)
    
    # Find SIN in the results
    sin_path = next((dest for dest in reachable if dest['airport'] == 'SIN'), None)
    
    if sin_path:
        print("\nDebug: Found path to SIN:")
        print(f"Total hours: {sin_path['flying_hours']}")
        print("Path details:")
        for detail in sin_path['path_details']:
            if detail.get('from'):
                print(f"  {detail['from']['airport']} -> {detail['to']['airport']} ({detail['flying_hours']} hours)")
            elif detail.get('layover'):
                print(f"  Layover in {detail['layover']['airport']}: {detail['layover']['hours']} hours")
    else:
        print("\nDebug: No path found to SIN")
    
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True) 