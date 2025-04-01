from flask import Flask, render_template, jsonify, request
from flight_data import AIRPORTS, FLIGHTS
import networkx as nx
from datetime import datetime, timedelta
import os

app = Flask(__name__)

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def calculate_flying_hours(departure, arrival):
    dep_time = parse_time(departure)
    arr_time = parse_time(arrival)
    
    # Handle overnight flights
    if arr_time < dep_time:
        arr_time += timedelta(days=1)
    
    return (arr_time - dep_time).total_seconds() / 3600

def find_reachable_destinations(start_airport, max_hours):
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add all airports as nodes
    for airport in AIRPORTS:
        G.add_node(airport, **AIRPORTS[airport])
    
    # Add edges with flight information
    for flight in FLIGHTS:
        G.add_edge(
            flight['from'],
            flight['to'],
            departure=flight['departure'],
            arrival=flight['arrival'],
            flying_hours=flight['flying_hours']
        )
    
    # Find all paths from start airport
    reachable = []
    visited = {}  # Track best times for each airport
    
    def process_path(path, total_hours, path_details):
        if total_hours > max_hours:
            return
        
        current = path[-1]
        if current not in visited or total_hours < visited[current]:
            visited[current] = total_hours
            
            # Add to reachable destinations if it's not the start airport
            if current != start_airport:
                reachable.append({
                    'airport': current,
                    'city': AIRPORTS[current]['city'],
                    'country': AIRPORTS[current].get('country', 'Unknown'),
                    'coordinates': AIRPORTS[current]['coordinates'],
                    'flying_hours': total_hours,
                    'hops': len(path) - 1,
                    'path_details': path_details
                })
            
            # Explore next possible flights
            for _, next_airport, data in G.edges(current, data=True):
                if next_airport not in path:  # Avoid cycles
                    new_path = path + [next_airport]
                    new_details = path_details + [{
                        'from': {
                            'airport': current,
                            'time': data['departure']
                        },
                        'to': {
                            'airport': next_airport,
                            'time': data['arrival']
                        },
                        'flying_hours': data['flying_hours']
                    }]
                    
                    # Add layover information if needed
                    if len(new_path) > 2:
                        layover_airport = new_path[-2]
                        layover_time = calculate_flying_hours(
                            G.edges[new_path[-3], layover_airport]['arrival'],
                            G.edges[layover_airport, next_airport]['departure']
                        )
                        new_details[-1]['layover'] = {
                            'airport': layover_airport,
                            'hours': layover_time
                        }
                    
                    process_path(new_path, total_hours + data['flying_hours'], new_details)
    
    # Start path finding from the start airport
    process_path([start_airport], 0, [])
    
    # Sort reachable destinations by flying hours
    reachable.sort(key=lambda x: x['flying_hours'])
    
    return {
        'start': AIRPORTS[start_airport],
        'reachable': reachable,
        'airports': AIRPORTS
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/reachable')
def get_reachable():
    hours = float(request.args.get('hours', 0))
    departure = request.args.get('departure', 'JFK')
    
    if departure not in AIRPORTS:
        return jsonify({'error': 'Invalid departure airport'}), 400
    
    return jsonify(find_reachable_destinations(departure, hours))

@app.route('/api/airports')
def get_airports():
    return jsonify(AIRPORTS)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 