from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from datetime import datetime, timedelta
import math
from collections import defaultdict, deque

app = Flask(__name__)
CORS(app)

# Sample flight data with more connections
sample_flights = [
    # Direct flights from JFK
    {
        "id": "FL001",
        "airline": "Airline A",
        "flightNumber": "AA123",
        "departure": {
            "city": "New York",
            "airport": "JFK",
            "time": "2024-03-20T10:00:00",
            "coordinates": [-73.7781, 40.6413]
        },
        "arrival": {
            "city": "London",
            "airport": "LHR",
            "time": "2024-03-20T22:00:00",
            "coordinates": [-0.4543, 51.4700]
        }
    },
    {
        "id": "FL002",
        "airline": "Airline B",
        "flightNumber": "BB456",
        "departure": {
            "city": "New York",
            "airport": "JFK",
            "time": "2024-03-20T11:00:00",
            "coordinates": [-73.7781, 40.6413]
        },
        "arrival": {
            "city": "Paris",
            "airport": "CDG",
            "time": "2024-03-20T23:00:00",
            "coordinates": [2.5488, 49.0097]
        }
    },
    {
        "id": "FL003",
        "airline": "Airline C",
        "flightNumber": "CC789",
        "departure": {
            "city": "New York",
            "airport": "JFK",
            "time": "2024-03-20T12:00:00",
            "coordinates": [-73.7781, 40.6413]
        },
        "arrival": {
            "city": "Tokyo",
            "airport": "NRT",
            "time": "2024-03-21T16:00:00",
            "coordinates": [140.3861, 35.7720]
        }
    },
    {
        "id": "FL004",
        "airline": "Airline D",
        "flightNumber": "DD101",
        "departure": {
            "city": "New York",
            "airport": "JFK",
            "time": "2024-03-20T13:00:00",
            "coordinates": [-73.7781, 40.6413]
        },
        "arrival": {
            "city": "Dubai",
            "airport": "DXB",
            "time": "2024-03-21T07:00:00",
            "coordinates": [55.2708, 25.2532]
        }
    },
    # New direct flight from JFK to LAX
    {
        "id": "FL010",
        "airline": "Airline J",
        "flightNumber": "JJ707",
        "departure": {
            "city": "New York",
            "airport": "JFK",
            "time": "2024-03-20T14:00:00",
            "coordinates": [-73.7781, 40.6413]
        },
        "arrival": {
            "city": "Los Angeles",
            "airport": "LAX",
            "time": "2024-03-20T17:00:00",
            "coordinates": [-118.4085, 33.9416]
        }
    },
    # New direct flight from JFK to São Paulo
    {
        "id": "FL014",
        "airline": "Airline N",
        "flightNumber": "NN202",
        "departure": {
            "city": "New York",
            "airport": "JFK",
            "time": "2024-03-20T15:00:00",
            "coordinates": [-73.7781, 40.6413]
        },
        "arrival": {
            "city": "São Paulo",
            "airport": "GRU",
            "time": "2024-03-21T02:00:00",
            "coordinates": [-46.6333, -23.5505]
        }
    },
    # New direct flight from JFK to Sydney
    {
        "id": "FL015",
        "airline": "Airline O",
        "flightNumber": "OO303",
        "departure": {
            "city": "New York",
            "airport": "JFK",
            "time": "2024-03-20T16:00:00",
            "coordinates": [-73.7781, 40.6413]
        },
        "arrival": {
            "city": "Sydney",
            "airport": "SYD",
            "time": "2024-03-22T06:00:00",
            "coordinates": [151.2093, -33.8688]
        }
    },
    # Connecting flights from LHR
    {
        "id": "FL005",
        "airline": "Airline E",
        "flightNumber": "EE202",
        "departure": {
            "city": "London",
            "airport": "LHR",
            "time": "2024-03-20T23:00:00",
            "coordinates": [-0.4543, 51.4700]
        },
        "arrival": {
            "city": "Paris",
            "airport": "CDG",
            "time": "2024-03-21T01:00:00",
            "coordinates": [2.5488, 49.0097]
        }
    },
    {
        "id": "FL006",
        "airline": "Airline F",
        "flightNumber": "FF303",
        "departure": {
            "city": "London",
            "airport": "LHR",
            "time": "2024-03-21T00:00:00",
            "coordinates": [-0.4543, 51.4700]
        },
        "arrival": {
            "city": "Amsterdam",
            "airport": "AMS",
            "time": "2024-03-21T02:00:00",
            "coordinates": [4.7639, 52.3086]
        }
    },
    # New connecting flights from LHR
    {
        "id": "FL016",
        "airline": "Airline P",
        "flightNumber": "PP404",
        "departure": {
            "city": "London",
            "airport": "LHR",
            "time": "2024-03-21T01:00:00",
            "coordinates": [-0.4543, 51.4700]
        },
        "arrival": {
            "city": "Cairo",
            "airport": "CAI",
            "time": "2024-03-21T07:00:00",
            "coordinates": [31.2357, 30.0444]
        }
    },
    # Connecting flights from CDG
    {
        "id": "FL007",
        "airline": "Airline G",
        "flightNumber": "GG404",
        "departure": {
            "city": "Paris",
            "airport": "CDG",
            "time": "2024-03-21T02:00:00",
            "coordinates": [2.5488, 49.0097]
        },
        "arrival": {
            "city": "Rome",
            "airport": "FCO",
            "time": "2024-03-21T04:00:00",
            "coordinates": [12.2468, 41.8045]
        }
    },
    # New connecting flights from CDG
    {
        "id": "FL017",
        "airline": "Airline Q",
        "flightNumber": "QQ505",
        "departure": {
            "city": "Paris",
            "airport": "CDG",
            "time": "2024-03-21T03:00:00",
            "coordinates": [2.5488, 49.0097]
        },
        "arrival": {
            "city": "Mumbai",
            "airport": "BOM",
            "time": "2024-03-21T15:00:00",
            "coordinates": [72.8777, 19.0760]
        }
    },
    # Connecting flights from NRT
    {
        "id": "FL008",
        "airline": "Airline H",
        "flightNumber": "HH505",
        "departure": {
            "city": "Tokyo",
            "airport": "NRT",
            "time": "2024-03-21T17:00:00",
            "coordinates": [140.3861, 35.7720]
        },
        "arrival": {
            "city": "Seoul",
            "airport": "ICN",
            "time": "2024-03-21T19:00:00",
            "coordinates": [126.4505, 37.4602]
        }
    },
    # New connecting flights from NRT
    {
        "id": "FL018",
        "airline": "Airline R",
        "flightNumber": "RR606",
        "departure": {
            "city": "Tokyo",
            "airport": "NRT",
            "time": "2024-03-21T18:00:00",
            "coordinates": [140.3861, 35.7720]
        },
        "arrival": {
            "city": "Bangkok",
            "airport": "BKK",
            "time": "2024-03-22T00:00:00",
            "coordinates": [100.5018, 13.7563]
        }
    },
    # Connecting flights from DXB
    {
        "id": "FL009",
        "airline": "Airline I",
        "flightNumber": "II606",
        "departure": {
            "city": "Dubai",
            "airport": "DXB",
            "time": "2024-03-21T08:00:00",
            "coordinates": [55.2708, 25.2532]
        },
        "arrival": {
            "city": "Singapore",
            "airport": "SIN",
            "time": "2024-03-21T20:00:00",
            "coordinates": [103.8198, 1.3644]
        }
    },
    # New connecting flights from DXB
    {
        "id": "FL019",
        "airline": "Airline S",
        "flightNumber": "SS707",
        "departure": {
            "city": "Dubai",
            "airport": "DXB",
            "time": "2024-03-21T09:00:00",
            "coordinates": [55.2708, 25.2532]
        },
        "arrival": {
            "city": "Johannesburg",
            "airport": "JNB",
            "time": "2024-03-21T17:00:00",
            "coordinates": [28.0473, -26.2041]
        }
    },
    # New connecting flights from AMS
    {
        "id": "FL011",
        "airline": "Airline K",
        "flightNumber": "KK808",
        "departure": {
            "city": "Amsterdam",
            "airport": "AMS",
            "time": "2024-03-21T03:00:00",
            "coordinates": [4.7639, 52.3086]
        },
        "arrival": {
            "city": "Beijing",
            "airport": "PEK",
            "time": "2024-03-21T22:00:00",
            "coordinates": [116.4074, 39.9042]
        }
    },
    # New connecting flights from LAX
    {
        "id": "FL012",
        "airline": "Airline L",
        "flightNumber": "LL909",
        "departure": {
            "city": "Los Angeles",
            "airport": "LAX",
            "time": "2024-03-20T18:00:00",
            "coordinates": [-118.4085, 33.9416]
        },
        "arrival": {
            "city": "Beijing",
            "airport": "PEK",
            "time": "2024-03-21T22:00:00",
            "coordinates": [116.4074, 39.9042]
        }
    },
    # New connecting flights from PEK
    {
        "id": "FL013",
        "airline": "Airline M",
        "flightNumber": "MM101",
        "departure": {
            "city": "Beijing",
            "airport": "PEK",
            "time": "2024-03-21T23:00:00",
            "coordinates": [116.4074, 39.9042]
        },
        "arrival": {
            "city": "Singapore",
            "airport": "SIN",
            "time": "2024-03-22T04:00:00",
            "coordinates": [103.8198, 1.3644]
        }
    },
    # New connecting flights from GRU
    {
        "id": "FL020",
        "airline": "Airline T",
        "flightNumber": "TT808",
        "departure": {
            "city": "São Paulo",
            "airport": "GRU",
            "time": "2024-03-21T03:00:00",
            "coordinates": [-46.6333, -23.5505]
        },
        "arrival": {
            "city": "Buenos Aires",
            "airport": "EZE",
            "time": "2024-03-21T05:00:00",
            "coordinates": [-58.3816, -34.6037]
        }
    },
    # New connecting flights from SYD
    {
        "id": "FL021",
        "airline": "Airline U",
        "flightNumber": "UU909",
        "departure": {
            "city": "Sydney",
            "airport": "SYD",
            "time": "2024-03-22T07:00:00",
            "coordinates": [151.2093, -33.8688]
        },
        "arrival": {
            "city": "Auckland",
            "airport": "AKL",
            "time": "2024-03-22T09:00:00",
            "coordinates": [174.7633, -36.8485]
        }
    }
]

def build_flight_network():
    """Build a graph representation of the flight network."""
    network = defaultdict(list)
    
    for flight in sample_flights:
        dep_airport = flight['departure']['airport']
        arr_airport = flight['arrival']['airport']
        
        # Calculate flying hours
        dep_time = datetime.fromisoformat(flight['departure']['time'].replace('Z', '+00:00'))
        arr_time = datetime.fromisoformat(flight['arrival']['time'].replace('Z', '+00:00'))
        flying_hours = (arr_time - dep_time).total_seconds() / 3600
        
        # Add edge to network
        network[dep_airport].append({
            'destination': arr_airport,
            'flying_hours': flying_hours,
            'flight': flight
        })
    
    return network

def find_reachable_destinations(start_airport, max_hours):
    """Find all reachable destinations within max_hours using BFS with path optimization."""
    network = build_flight_network()
    reachable = {}  # Use dict to store best paths to each destination
    visited = set()
    queue = deque([(start_airport, 0, [], [])])  # (airport, total_hours, path, flights)
    
    while queue:
        current_airport, total_hours, path, flights = queue.popleft()
        
        if current_airport in visited:
            continue
            
        visited.add(current_airport)
        
        # If this is not the starting airport, update reachable destinations
        if current_airport != start_airport:
            last_flight = flights[-1]
            dest_key = current_airport
            
            # Only update if this path is better (shorter) than existing path
            if dest_key not in reachable or total_hours < reachable[dest_key]['flying_hours']:
                reachable[dest_key] = {
                    'airport': current_airport,
                    'city': last_flight['arrival']['city'],
                    'coordinates': last_flight['arrival']['coordinates'],
                    'flying_hours': total_hours,
                    'hops': len(flights),
                    'departure_time': last_flight['departure']['time']
                }
        
        # Explore all possible next flights
        for connection in network[current_airport]:
            next_airport = connection['destination']
            next_hours = total_hours + connection['flying_hours']
            
            # Only continue if we haven't exceeded max hours
            if next_hours <= max_hours:
                new_path = path + [current_airport]
                new_flights = flights + [connection['flight']]
                queue.append((next_airport, next_hours, new_path, new_flights))
    
    return list(reachable.values())

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/reachable')
def get_reachable():
    hours = float(request.args.get('hours', 0))
    reachable = find_reachable_destinations('JFK', hours)
    return jsonify({
        'start': {
            'airport': 'JFK',
            'city': 'New York',
            'coordinates': [-73.7781, 40.6413]
        },
        'reachable': reachable
    })

if __name__ == '__main__':
    app.run(debug=True) 