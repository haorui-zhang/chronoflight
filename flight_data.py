# Airport coordinates with major hubs worldwide
AIRPORTS = {
    # North America
    "JFK": {"city": "New York", "coordinates": [-73.7789, 40.6413]},
    "LAX": {"city": "Los Angeles", "coordinates": [-118.4085, 33.9416]},
    "ORD": {"city": "Chicago", "coordinates": [-87.9048, 41.9786]},
    "DFW": {"city": "Dallas", "coordinates": [-97.0380, 32.8998]},
    "MIA": {"city": "Miami", "coordinates": [-80.2906, 25.7932]},
    "SFO": {"city": "San Francisco", "coordinates": [-122.3748, 37.6188]},
    "SEA": {"city": "Seattle", "coordinates": [-122.3088, 47.4502]},
    "BOS": {"city": "Boston", "coordinates": [-71.0202, 42.3656]},
    "LAS": {"city": "Las Vegas", "coordinates": [-115.1398, 36.0840]},
    "DEN": {"city": "Denver", "coordinates": [-104.6732, 39.8561]},
    
    # Europe
    "LHR": {"city": "London", "coordinates": [-0.4614, 51.4700]},
    "CDG": {"city": "Paris", "coordinates": [2.5486, 49.0097]},
    "AMS": {"city": "Amsterdam", "coordinates": [4.7639, 52.3086]},
    "FRA": {"city": "Frankfurt", "coordinates": [8.5705, 50.0379]},
    "MAD": {"city": "Madrid", "coordinates": [-3.5668, 40.4983]},
    "FCO": {"city": "Rome", "coordinates": [12.2467, 41.8045]},
    "IST": {"city": "Istanbul", "coordinates": [28.8146, 41.2751]},
    "MUC": {"city": "Munich", "coordinates": [11.7861, 48.3538]},
    "BCN": {"city": "Barcelona", "coordinates": [2.0785, 41.2974]},
    "VIE": {"city": "Vienna", "coordinates": [16.5697, 48.1102]},
    
    # Asia
    "NRT": {"city": "Tokyo", "coordinates": [140.3861, 35.7720]},
    "HND": {"city": "Tokyo", "coordinates": [139.7811, 35.5494]},
    "PEK": {"city": "Beijing", "coordinates": [116.5975, 40.0799]},
    "PVG": {"city": "Shanghai", "coordinates": [121.8053, 31.1443]},
    "HKG": {"city": "Hong Kong", "coordinates": [113.9146, 22.3080]},
    "SIN": {"city": "Singapore", "coordinates": [103.9944, 1.3644]},
    "ICN": {"city": "Seoul", "coordinates": [126.4505, 37.4602]},
    "BKK": {"city": "Bangkok", "coordinates": [100.7471, 13.6900]},
    "KUL": {"city": "Kuala Lumpur", "coordinates": [101.6937, 2.7456]},
    "DEL": {"city": "Delhi", "coordinates": [77.1040, 28.5562]},
    
    # Middle East
    "DXB": {"city": "Dubai", "coordinates": [55.3644, 25.2532]},
    "AUH": {"city": "Abu Dhabi", "coordinates": [54.6511, 24.4331]},
    "DOH": {"city": "Doha", "coordinates": [51.6081, 25.2734]},
    "JED": {"city": "Jeddah", "coordinates": [39.1566, 21.6711]},
    "RUH": {"city": "Riyadh", "coordinates": [46.6988, 24.9576]},
    
    # Oceania
    "SYD": {"city": "Sydney", "coordinates": [151.1772, -33.9399]},
    "MEL": {"city": "Melbourne", "country": "Australia", "coordinates": [144.8433, -37.6733]},
    "BNE": {"city": "Brisbane", "country": "Australia", "coordinates": [153.1171, -27.4710]},
    "AKL": {"city": "Auckland", "coordinates": [174.7689, -37.0081]},
    
    # South America
    "GRU": {"city": "São Paulo", "coordinates": [-46.6333, -23.4356]},
    "EZE": {"city": "Buenos Aires", "coordinates": [-58.5358, -34.8222]},
    "LIM": {"city": "Lima", "coordinates": [-77.1143, -12.0219]},
    "SCL": {"city": "Santiago", "coordinates": [-70.7858, -33.3929]},
    "BOG": {"city": "Bogota", "coordinates": [-74.1469, 4.7016]},
    
    # Africa
    "JNB": {"city": "Johannesburg", "coordinates": [28.2460, -26.1367]},
    "CPT": {"city": "Cape Town", "coordinates": [18.6017, -33.9715]},
    "CAI": {"city": "Cairo", "coordinates": [31.4056, 30.1219]},
    "NBO": {"city": "Nairobi", "coordinates": [36.9278, -1.3192]},
    "ADD": {"city": "Addis Ababa", "coordinates": [38.7990, 8.9779]},
    
    # Additional Australian airports
    "PER": {"city": "Perth", "country": "Australia", "coordinates": [115.9789, -31.9404]},
    "ADL": {"city": "Adelaide", "country": "Australia", "coordinates": [138.5306, -34.9285]},
    "OOL": {"city": "Gold Coast", "country": "Australia", "coordinates": [153.5050, -28.1644]},
    "CNS": {"city": "Cairns", "country": "Australia", "coordinates": [145.7544, -16.8858]},
    
    # Additional Indonesian airports
    "CGK": {"city": "Jakarta", "country": "Indonesia", "coordinates": [106.8456, -6.1256]},
    "DPS": {"city": "Denpasar", "country": "Indonesia", "coordinates": [115.1672, -8.7467]},
    "MES": {"city": "Medan", "country": "Indonesia", "coordinates": [98.6719, 3.5581]},
    "UPG": {"city": "Makassar", "country": "Indonesia", "coordinates": [119.5540, -5.0616]},
    "SUB": {"city": "Surabaya", "country": "Indonesia", "coordinates": [112.7778, -7.3798]},
    "LOP": {"city": "Lombok", "country": "Indonesia", "coordinates": [116.2767, -8.7573]},
    
    # Pacific Islands
    "HNL": {"city": "Honolulu", "country": "Hawaii", "coordinates": [-157.9225, 21.3187]},
    "PPT": {"city": "Papeete", "country": "French Polynesia", "coordinates": [-149.6068, -17.5567]},
    "RAR": {"city": "Rarotonga", "country": "Cook Islands", "coordinates": [-159.8061, -21.2027]},
    "NAN": {"city": "Nadi", "country": "Fiji", "coordinates": [177.4434, -17.7551]},
    "TBU": {"city": "Nuku'alofa", "country": "Tonga", "coordinates": [-175.1496, -21.2411]},
    "APW": {"city": "Apia", "country": "Samoa", "coordinates": [-171.7600, -13.8297]},
    "IPC": {"city": "Easter Island", "country": "Chile", "coordinates": [-109.4217, -27.1648]},
}

# Complete flight network with all routes
FLIGHTS = [
    # Domestic US flights
    {"from": "JFK", "to": "LAX", "departure": "09:00", "arrival": "12:00", "flying_hours": 5.0},
    {"from": "JFK", "to": "ORD", "departure": "10:00", "arrival": "12:00", "flying_hours": 2.5},
    {"from": "JFK", "to": "LAS", "departure": "16:00", "arrival": "19:00", "flying_hours": 5.0},
    {"from": "JFK", "to": "DEN", "departure": "17:00", "arrival": "19:30", "flying_hours": 3.5},
    
    # Transatlantic flights from JFK
    {"from": "JFK", "to": "LHR", "departure": "18:00", "arrival": "06:00", "flying_hours": 7.0},
    {"from": "JFK", "to": "MAD", "departure": "22:00", "arrival": "10:00", "flying_hours": 7.0},
    
    # Transpacific flights from JFK
    {"from": "JFK", "to": "NRT", "departure": "11:00", "arrival": "14:00", "flying_hours": 14.0},
    {"from": "JFK", "to": "PEK", "departure": "12:00", "arrival": "15:00", "flying_hours": 14.0},
    {"from": "JFK", "to": "PVG", "departure": "13:00", "arrival": "16:00", "flying_hours": 15.0},
    {"from": "JFK", "to": "HKG", "departure": "14:00", "arrival": "17:00", "flying_hours": 16.0},
    {"from": "JFK", "to": "SIN", "departure": "15:00", "arrival": "19:00", "flying_hours": 18.0},
    
    # Alternative routes from JFK to Asia
    {"from": "JFK", "to": "DXB", "departure": "16:00", "arrival": "12:00", "flying_hours": 13.0},
    {"from": "JFK", "to": "AUH", "departure": "17:00", "arrival": "13:00", "flying_hours": 13.0},
    {"from": "JFK", "to": "DOH", "departure": "18:00", "arrival": "14:00", "flying_hours": 13.0},
    
    # Alternative routes from JFK to Europe
    {"from": "JFK", "to": "MUC", "departure": "23:00", "arrival": "11:00", "flying_hours": 8.0},
    {"from": "JFK", "to": "BCN", "departure": "00:00", "arrival": "12:00", "flying_hours": 8.0},
    {"from": "JFK", "to": "VIE", "departure": "01:00", "arrival": "13:00", "flying_hours": 8.5},
    
    # Alternative routes from JFK to South America
    {"from": "JFK", "to": "GRU", "departure": "02:00", "arrival": "11:00", "flying_hours": 9.0},
    {"from": "JFK", "to": "BOG", "departure": "06:00", "arrival": "11:00", "flying_hours": 5.0},
    
    # Alternative routes from JFK to Africa
    {"from": "JFK", "to": "JNB", "departure": "07:00", "arrival": "18:00", "flying_hours": 15.0},
    {"from": "JFK", "to": "NBO", "departure": "10:00", "arrival": "22:00", "flying_hours": 16.0},
    {"from": "JFK", "to": "ADD", "departure": "11:00", "arrival": "21:00", "flying_hours": 14.0},
    
    # Connections from LHR
    {"from": "LHR", "to": "CDG", "departure": "08:00", "arrival": "10:00", "flying_hours": 1.5},
    {"from": "LHR", "to": "AMS", "departure": "09:00", "arrival": "11:00", "flying_hours": 1.5},
    {"from": "LHR", "to": "FRA", "departure": "10:00", "arrival": "12:00", "flying_hours": 1.5},
    {"from": "LHR", "to": "MAD", "departure": "11:00", "arrival": "14:00", "flying_hours": 2.5},
    {"from": "LHR", "to": "FCO", "departure": "12:00", "arrival": "15:00", "flying_hours": 2.5},
    {"from": "LHR", "to": "IST", "departure": "13:00", "arrival": "18:00", "flying_hours": 4.0},
    {"from": "LHR", "to": "DXB", "departure": "14:00", "arrival": "00:00", "flying_hours": 7.0},
    {"from": "LHR", "to": "SIN", "departure": "15:00", "arrival": "10:00", "flying_hours": 13.0},
    {"from": "LHR", "to": "HKG", "departure": "16:00", "arrival": "11:00", "flying_hours": 12.0},
    {"from": "LHR", "to": "SYD", "departure": "17:00", "arrival": "19:00", "flying_hours": 22.0},
    {"from": "LHR", "to": "MUC", "departure": "18:00", "arrival": "20:30", "flying_hours": 2.0},
    {"from": "LHR", "to": "BCN", "departure": "19:00", "arrival": "22:00", "flying_hours": 2.0},
    {"from": "LHR", "to": "VIE", "departure": "20:00", "arrival": "23:00", "flying_hours": 2.0},
    {"from": "LHR", "to": "AUH", "departure": "21:00", "arrival": "07:00", "flying_hours": 7.0},
    {"from": "LHR", "to": "DOH", "departure": "22:00", "arrival": "08:00", "flying_hours": 7.0},
    
    # Connections from CDG
    {"from": "CDG", "to": "AMS", "departure": "08:00", "arrival": "09:30", "flying_hours": 1.5},
    {"from": "CDG", "to": "FRA", "departure": "09:00", "arrival": "10:30", "flying_hours": 1.5},
    {"from": "CDG", "to": "MAD", "departure": "10:00", "arrival": "12:30", "flying_hours": 2.5},
    {"from": "CDG", "to": "FCO", "departure": "11:00", "arrival": "13:00", "flying_hours": 2.0},
    {"from": "CDG", "to": "DXB", "departure": "12:00", "arrival": "20:00", "flying_hours": 6.5},
    {"from": "CDG", "to": "PEK", "departure": "13:00", "arrival": "05:00", "flying_hours": 10.0},
    {"from": "CDG", "to": "PVG", "departure": "14:00", "arrival": "06:00", "flying_hours": 11.0},
    {"from": "CDG", "to": "SIN", "departure": "15:00", "arrival": "09:00", "flying_hours": 12.0},
    {"from": "CDG", "to": "MUC", "departure": "16:00", "arrival": "18:00", "flying_hours": 1.5},
    {"from": "CDG", "to": "BCN", "departure": "17:00", "arrival": "19:00", "flying_hours": 2.0},
    {"from": "CDG", "to": "VIE", "departure": "18:00", "arrival": "20:00", "flying_hours": 2.0},
    {"from": "CDG", "to": "AUH", "departure": "19:00", "arrival": "05:00", "flying_hours": 7.0},
    {"from": "CDG", "to": "DOH", "departure": "20:00", "arrival": "06:00", "flying_hours": 7.0},
    
    # Connections from DXB
    {"from": "DXB", "to": "SIN", "departure": "01:00", "arrival": "13:00", "flying_hours": 7.0},
    {"from": "DXB", "to": "HKG", "departure": "02:00", "arrival": "14:00", "flying_hours": 7.0},
    {"from": "DXB", "to": "SYD", "departure": "03:00", "arrival": "23:00", "flying_hours": 13.0},
    {"from": "DXB", "to": "JNB", "departure": "04:00", "arrival": "10:00", "flying_hours": 8.0},
    {"from": "DXB", "to": "CPT", "departure": "05:00", "arrival": "12:00", "flying_hours": 9.0},
    {"from": "DXB", "to": "NBO", "departure": "06:00", "arrival": "10:00", "flying_hours": 5.0},
    {"from": "DXB", "to": "AUH", "departure": "07:00", "arrival": "08:00", "flying_hours": 1.0},
    {"from": "DXB", "to": "DOH", "departure": "08:00", "arrival": "09:00", "flying_hours": 1.0},
    {"from": "DXB", "to": "JED", "departure": "09:00", "arrival": "10:30", "flying_hours": 2.0},
    {"from": "DXB", "to": "RUH", "departure": "10:00", "arrival": "11:30", "flying_hours": 2.0},
    
    # Connections from SIN
    {"from": "SIN", "to": "HKG", "departure": "08:00", "arrival": "12:00", "flying_hours": 4.0},
    {"from": "SIN", "to": "PEK", "departure": "09:00", "arrival": "15:00", "flying_hours": 6.0},
    {"from": "SIN", "to": "PVG", "departure": "10:00", "arrival": "16:00", "flying_hours": 6.0},
    {"from": "SIN", "to": "NRT", "departure": "11:00", "arrival": "18:00", "flying_hours": 7.0},
    {"from": "SIN", "to": "SYD", "departure": "12:00", "arrival": "22:00", "flying_hours": 8.0},
    {"from": "SIN", "to": "MEL", "departure": "13:00", "arrival": "23:00", "flying_hours": 8.0},
    {"from": "SIN", "to": "BNE", "departure": "14:00", "arrival": "00:00", "flying_hours": 8.0},
    {"from": "SIN", "to": "DEL", "departure": "15:00", "arrival": "18:00", "flying_hours": 5.0},
    {"from": "SIN", "to": "BKK", "departure": "16:00", "arrival": "17:30", "flying_hours": 2.0},
    {"from": "SIN", "to": "KUL", "departure": "17:00", "arrival": "18:00", "flying_hours": 1.0},
    {"from": "SIN", "to": "ICN", "departure": "18:00", "arrival": "05:00", "flying_hours": 6.0},
    {"from": "SIN", "to": "CAI", "departure": "19:00", "arrival": "05:00", "flying_hours": 10.0},
    {"from": "SIN", "to": "ADD", "departure": "20:00", "arrival": "05:00", "flying_hours": 9.0},
    
    # Connections from NRT
    {"from": "NRT", "to": "PEK", "departure": "08:00", "arrival": "10:00", "flying_hours": 3.0},
    {"from": "NRT", "to": "PVG", "departure": "09:00", "arrival": "11:00", "flying_hours": 3.0},
    {"from": "NRT", "to": "HKG", "departure": "10:00", "arrival": "13:00", "flying_hours": 4.0},
    {"from": "NRT", "to": "SIN", "departure": "11:00", "arrival": "17:00", "flying_hours": 7.0},
    {"from": "NRT", "to": "SYD", "departure": "12:00", "arrival": "22:00", "flying_hours": 10.0},
    {"from": "NRT", "to": "LAX", "departure": "13:00", "arrival": "08:00", "flying_hours": 11.0},
    {"from": "NRT", "to": "SFO", "departure": "14:00", "arrival": "09:00", "flying_hours": 11.0},
    {"from": "NRT", "to": "SEA", "departure": "15:00", "arrival": "10:00", "flying_hours": 10.0},
    {"from": "NRT", "to": "ICN", "departure": "16:00", "arrival": "18:00", "flying_hours": 2.0},
    {"from": "NRT", "to": "DEL", "departure": "17:00", "arrival": "23:00", "flying_hours": 8.0},
    {"from": "NRT", "to": "BKK", "departure": "18:00", "arrival": "22:00", "flying_hours": 6.0},
    {"from": "NRT", "to": "KUL", "departure": "19:00", "arrival": "00:00", "flying_hours": 7.0},
    
    # Connections from PEK
    {"from": "PEK", "to": "PVG", "departure": "08:00", "arrival": "10:00", "flying_hours": 2.5},
    {"from": "PEK", "to": "HKG", "departure": "09:00", "arrival": "12:30", "flying_hours": 3.5},
    {"from": "PEK", "to": "SIN", "departure": "10:00", "arrival": "16:00", "flying_hours": 6.0},
    {"from": "PEK", "to": "NRT", "departure": "11:00", "arrival": "15:00", "flying_hours": 3.0},
    {"from": "PEK", "to": "SYD", "departure": "12:00", "arrival": "23:00", "flying_hours": 11.0},
    {"from": "PEK", "to": "LAX", "departure": "13:00", "arrival": "10:00", "flying_hours": 12.0},
    {"from": "PEK", "to": "SFO", "departure": "14:00", "arrival": "11:00", "flying_hours": 12.0},
    {"from": "PEK", "to": "JFK", "departure": "15:00", "arrival": "17:00", "flying_hours": 14.0},
    {"from": "PEK", "to": "ICN", "departure": "16:00", "arrival": "18:00", "flying_hours": 2.0},
    {"from": "PEK", "to": "DEL", "departure": "17:00", "arrival": "23:00", "flying_hours": 8.0},
    {"from": "PEK", "to": "BKK", "departure": "18:00", "arrival": "22:00", "flying_hours": 6.0},
    {"from": "PEK", "to": "KUL", "departure": "19:00", "arrival": "00:00", "flying_hours": 7.0},
    
    # Connections from SYD
    {"from": "SYD", "to": "MEL", "departure": "08:00", "arrival": "09:30", "flying_hours": 1.5},
    {"from": "SYD", "to": "BNE", "departure": "09:00", "arrival": "10:00", "flying_hours": 1.0},
    {"from": "SYD", "to": "AKL", "departure": "10:00", "arrival": "15:00", "flying_hours": 3.0},
    {"from": "SYD", "to": "SIN", "departure": "11:00", "arrival": "17:00", "flying_hours": 8.0},
    {"from": "SYD", "to": "HKG", "departure": "12:00", "arrival": "19:00", "flying_hours": 9.0},
    {"from": "SYD", "to": "LAX", "departure": "13:00", "arrival": "10:00", "flying_hours": 15.0},
    {"from": "SYD", "to": "SFO", "departure": "14:00", "arrival": "11:00", "flying_hours": 15.0},
    {"from": "SYD", "to": "DXB", "departure": "15:00", "arrival": "02:00", "flying_hours": 14.0},
    {"from": "SYD", "to": "AKL", "departure": "16:00", "arrival": "21:00", "flying_hours": 3.0},
    {"from": "SYD", "to": "DEL", "departure": "17:00", "arrival": "02:00", "flying_hours": 13.0},
    {"from": "SYD", "to": "BKK", "departure": "18:00", "arrival": "00:00", "flying_hours": 9.0},
    {"from": "SYD", "to": "KUL", "departure": "19:00", "arrival": "01:00", "flying_hours": 8.0},
    
    # Connections from GRU
    {"from": "GRU", "to": "EZE", "departure": "08:00", "arrival": "10:00", "flying_hours": 2.0},
    {"from": "GRU", "to": "LIM", "departure": "09:00", "arrival": "12:00", "flying_hours": 4.0},
    {"from": "GRU", "to": "SCL", "departure": "10:00", "arrival": "13:00", "flying_hours": 4.0},
    {"from": "GRU", "to": "BOG", "departure": "11:00", "arrival": "15:00", "flying_hours": 5.0},
    {"from": "GRU", "to": "MIA", "departure": "12:00", "arrival": "19:00", "flying_hours": 8.0},
    {"from": "GRU", "to": "JFK", "departure": "13:00", "arrival": "21:00", "flying_hours": 9.0},
    {"from": "GRU", "to": "LHR", "departure": "14:00", "arrival": "05:00", "flying_hours": 11.0},
    {"from": "GRU", "to": "CDG", "departure": "15:00", "arrival": "06:00", "flying_hours": 11.0},
    {"from": "GRU", "to": "MIA", "departure": "16:00", "arrival": "23:00", "flying_hours": 8.0},
    {"from": "GRU", "to": "MAD", "departure": "17:00", "arrival": "06:00", "flying_hours": 10.0},
    {"from": "GRU", "to": "BCN", "departure": "18:00", "arrival": "07:00", "flying_hours": 10.0},
    {"from": "GRU", "to": "FCO", "departure": "19:00", "arrival": "08:00", "flying_hours": 11.0},
    
    # Connections from JNB
    {"from": "JNB", "to": "CPT", "departure": "08:00", "arrival": "10:00", "flying_hours": 2.0},
    {"from": "JNB", "to": "NBO", "departure": "09:00", "arrival": "12:00", "flying_hours": 4.0},
    {"from": "JNB", "to": "CAI", "departure": "10:00", "arrival": "16:00", "flying_hours": 7.0},
    {"from": "JNB", "to": "ADD", "departure": "11:00", "arrival": "15:00", "flying_hours": 5.0},
    {"from": "JNB", "to": "DXB", "departure": "12:00", "arrival": "22:00", "flying_hours": 8.0},
    {"from": "JNB", "to": "LHR", "departure": "13:00", "arrival": "22:00", "flying_hours": 11.0},
    {"from": "JNB", "to": "AMS", "departure": "14:00", "arrival": "23:00", "flying_hours": 11.0},
    {"from": "JNB", "to": "FRA", "departure": "15:00", "arrival": "00:00", "flying_hours": 11.0},
    {"from": "JNB", "to": "MUC", "departure": "16:00", "arrival": "00:00", "flying_hours": 10.0},
    {"from": "JNB", "to": "BCN", "departure": "17:00", "arrival": "01:00", "flying_hours": 10.0},
    {"from": "JNB", "to": "VIE", "departure": "18:00", "arrival": "02:00", "flying_hours": 10.0},
    {"from": "JNB", "to": "AUH", "departure": "19:00", "arrival": "05:00", "flying_hours": 8.0},
    {"from": "JNB", "to": "DOH", "departure": "20:00", "arrival": "06:00", "flying_hours": 8.0},
    
    # Domestic Australian flights
    {"from": "SYD", "to": "MEL", "departure": "08:00", "arrival": "09:30", "flying_hours": 1.5},
    {"from": "SYD", "to": "BNE", "departure": "09:00", "arrival": "10:00", "flying_hours": 1.0},
    {"from": "SYD", "to": "PER", "departure": "10:00", "arrival": "12:30", "flying_hours": 4.5},
    {"from": "SYD", "to": "ADL", "departure": "11:00", "arrival": "12:30", "flying_hours": 2.0},
    {"from": "SYD", "to": "OOL", "departure": "12:00", "arrival": "13:00", "flying_hours": 1.0},
    {"from": "SYD", "to": "CNS", "departure": "13:00", "arrival": "15:00", "flying_hours": 3.0},
    
    {"from": "MEL", "to": "BNE", "departure": "08:00", "arrival": "09:30", "flying_hours": 1.5},
    {"from": "MEL", "to": "PER", "departure": "09:00", "arrival": "11:30", "flying_hours": 4.0},
    {"from": "MEL", "to": "ADL", "departure": "10:00", "arrival": "11:00", "flying_hours": 1.0},
    {"from": "MEL", "to": "OOL", "departure": "11:00", "arrival": "12:30", "flying_hours": 1.5},
    {"from": "MEL", "to": "CNS", "departure": "12:00", "arrival": "14:30", "flying_hours": 3.5},
    
    {"from": "BNE", "to": "PER", "departure": "08:00", "arrival": "11:30", "flying_hours": 5.5},
    {"from": "BNE", "to": "ADL", "departure": "09:00", "arrival": "11:00", "flying_hours": 2.0},
    {"from": "BNE", "to": "OOL", "departure": "10:00", "arrival": "10:30", "flying_hours": 0.5},
    {"from": "BNE", "to": "CNS", "departure": "11:00", "arrival": "13:00", "flying_hours": 2.0},
    
    # Domestic Indonesian flights
    {"from": "CGK", "to": "DPS", "departure": "08:00", "arrival": "10:00", "flying_hours": 2.0},
    {"from": "CGK", "to": "MES", "departure": "09:00", "arrival": "11:00", "flying_hours": 2.0},
    {"from": "CGK", "to": "UPG", "departure": "10:00", "arrival": "13:00", "flying_hours": 3.0},
    {"from": "CGK", "to": "SUB", "departure": "11:00", "arrival": "12:30", "flying_hours": 1.5},
    {"from": "CGK", "to": "LOP", "departure": "12:00", "arrival": "14:00", "flying_hours": 2.0},
    
    {"from": "DPS", "to": "CGK", "departure": "08:00", "arrival": "10:00", "flying_hours": 2.0},
    {"from": "DPS", "to": "MES", "departure": "09:00", "arrival": "12:00", "flying_hours": 3.0},
    {"from": "DPS", "to": "UPG", "departure": "10:00", "arrival": "13:00", "flying_hours": 3.0},
    {"from": "DPS", "to": "SUB", "departure": "11:00", "arrival": "12:30", "flying_hours": 1.5},
    {"from": "DPS", "to": "LOP", "departure": "12:00", "arrival": "12:30", "flying_hours": 0.5},
    
    {"from": "MES", "to": "CGK", "departure": "08:00", "arrival": "10:00", "flying_hours": 2.0},
    {"from": "MES", "to": "DPS", "departure": "09:00", "arrival": "12:00", "flying_hours": 3.0},
    {"from": "MES", "to": "UPG", "departure": "10:00", "arrival": "13:00", "flying_hours": 3.0},
    {"from": "MES", "to": "SUB", "departure": "11:00", "arrival": "13:00", "flying_hours": 2.0},
    {"from": "MES", "to": "LOP", "departure": "12:00", "arrival": "14:00", "flying_hours": 2.0},
    
    # International connections to Australia and Indonesia
    {"from": "SIN", "to": "SYD", "departure": "08:00", "arrival": "18:00", "flying_hours": 8.0},
    {"from": "SIN", "to": "MEL", "departure": "09:00", "arrival": "19:00", "flying_hours": 8.0},
    {"from": "SIN", "to": "BNE", "departure": "10:00", "arrival": "20:00", "flying_hours": 8.0},
    {"from": "SIN", "to": "CGK", "departure": "11:00", "arrival": "12:00", "flying_hours": 1.0},
    {"from": "SIN", "to": "DPS", "departure": "12:00", "arrival": "14:00", "flying_hours": 2.0},
    
    {"from": "KUL", "to": "SYD", "departure": "08:00", "arrival": "19:00", "flying_hours": 9.0},
    {"from": "KUL", "to": "MEL", "departure": "09:00", "arrival": "20:00", "flying_hours": 9.0},
    {"from": "KUL", "to": "BNE", "departure": "10:00", "arrival": "21:00", "flying_hours": 9.0},
    {"from": "KUL", "to": "CGK", "departure": "11:00", "arrival": "12:00", "flying_hours": 1.0},
    {"from": "KUL", "to": "DPS", "departure": "12:00", "arrival": "14:00", "flying_hours": 2.0},
    
    {"from": "BKK", "to": "SYD", "departure": "08:00", "arrival": "19:00", "flying_hours": 9.0},
    {"from": "BKK", "to": "MEL", "departure": "09:00", "arrival": "20:00", "flying_hours": 9.0},
    {"from": "BKK", "to": "BNE", "departure": "10:00", "arrival": "21:00", "flying_hours": 9.0},
    {"from": "BKK", "to": "CGK", "departure": "11:00", "arrival": "13:00", "flying_hours": 2.0},
    {"from": "BKK", "to": "DPS", "departure": "12:00", "arrival": "15:00", "flying_hours": 3.0},
    
    # Pacific Island flights
    {"from": "HNL", "to": "PPT", "departure": "08:00", "arrival": "14:00", "flying_hours": 6.0},
    {"from": "HNL", "to": "RAR", "departure": "09:00", "arrival": "15:00", "flying_hours": 6.0},
    {"from": "HNL", "to": "NAN", "departure": "10:00", "arrival": "16:00", "flying_hours": 6.0},
    {"from": "HNL", "to": "TBU", "departure": "11:00", "arrival": "17:00", "flying_hours": 6.0},
    {"from": "HNL", "to": "APW", "departure": "12:00", "arrival": "18:00", "flying_hours": 6.0},
    {"from": "HNL", "to": "IPC", "departure": "13:00", "arrival": "19:00", "flying_hours": 6.0},
    
    {"from": "PPT", "to": "HNL", "departure": "08:00", "arrival": "14:00", "flying_hours": 6.0},
    {"from": "PPT", "to": "RAR", "departure": "09:00", "arrival": "11:00", "flying_hours": 2.0},
    {"from": "PPT", "to": "NAN", "departure": "10:00", "arrival": "14:00", "flying_hours": 4.0},
    {"from": "PPT", "to": "TBU", "departure": "11:00", "arrival": "15:00", "flying_hours": 4.0},
    {"from": "PPT", "to": "APW", "departure": "12:00", "arrival": "16:00", "flying_hours": 4.0},
    {"from": "PPT", "to": "IPC", "departure": "13:00", "arrival": "17:00", "flying_hours": 4.0},
    
    {"from": "NAN", "to": "HNL", "departure": "08:00", "arrival": "14:00", "flying_hours": 6.0},
    {"from": "NAN", "to": "PPT", "departure": "09:00", "arrival": "13:00", "flying_hours": 4.0},
    {"from": "NAN", "to": "RAR", "departure": "10:00", "arrival": "12:00", "flying_hours": 2.0},
    {"from": "NAN", "to": "TBU", "departure": "11:00", "arrival": "12:00", "flying_hours": 1.0},
    {"from": "NAN", "to": "APW", "departure": "12:00", "arrival": "14:00", "flying_hours": 2.0},
    {"from": "NAN", "to": "IPC", "departure": "13:00", "arrival": "17:00", "flying_hours": 4.0},
    
    {"from": "TBU", "to": "HNL", "departure": "08:00", "arrival": "14:00", "flying_hours": 6.0},
    {"from": "TBU", "to": "PPT", "departure": "09:00", "arrival": "13:00", "flying_hours": 4.0},
    {"from": "TBU", "to": "RAR", "departure": "10:00", "arrival": "12:00", "flying_hours": 2.0},
    {"from": "TBU", "to": "NAN", "departure": "11:00", "arrival": "12:00", "flying_hours": 1.0},
    {"from": "TBU", "to": "APW", "departure": "12:00", "arrival": "14:00", "flying_hours": 2.0},
    {"from": "TBU", "to": "IPC", "departure": "13:00", "arrival": "17:00", "flying_hours": 4.0},
    
    {"from": "APW", "to": "HNL", "departure": "08:00", "arrival": "14:00", "flying_hours": 6.0},
    {"from": "APW", "to": "PPT", "departure": "09:00", "arrival": "13:00", "flying_hours": 4.0},
    {"from": "APW", "to": "RAR", "departure": "10:00", "arrival": "12:00", "flying_hours": 2.0},
    {"from": "APW", "to": "NAN", "departure": "11:00", "arrival": "13:00", "flying_hours": 2.0},
    {"from": "APW", "to": "TBU", "departure": "12:00", "arrival": "14:00", "flying_hours": 2.0},
    {"from": "APW", "to": "IPC", "departure": "13:00", "arrival": "17:00", "flying_hours": 4.0},
    
    {"from": "IPC", "to": "HNL", "departure": "08:00", "arrival": "14:00", "flying_hours": 6.0},
    {"from": "IPC", "to": "PPT", "departure": "09:00", "arrival": "13:00", "flying_hours": 4.0},
    {"from": "IPC", "to": "RAR", "departure": "10:00", "arrival": "12:00", "flying_hours": 2.0},
    {"from": "IPC", "to": "NAN", "departure": "11:00", "arrival": "15:00", "flying_hours": 4.0},
    {"from": "IPC", "to": "TBU", "departure": "12:00", "arrival": "16:00", "flying_hours": 4.0},
    {"from": "IPC", "to": "APW", "departure": "13:00", "arrival": "17:00", "flying_hours": 4.0},
    
    # Connections from major hubs to Pacific Islands
    {"from": "LAX", "to": "HNL", "departure": "08:00", "arrival": "12:00", "flying_hours": 5.0},
    {"from": "SFO", "to": "HNL", "departure": "09:00", "arrival": "13:00", "flying_hours": 5.0},
    {"from": "SEA", "to": "HNL", "departure": "10:00", "arrival": "14:00", "flying_hours": 5.0},
    {"from": "SYD", "to": "HNL", "departure": "11:00", "arrival": "15:00", "flying_hours": 5.0},
    {"from": "AKL", "to": "HNL", "departure": "12:00", "arrival": "16:00", "flying_hours": 5.0},
    {"from": "NAN", "to": "SYD", "departure": "13:00", "arrival": "17:00", "flying_hours": 4.0},
    {"from": "NAN", "to": "AKL", "departure": "14:00", "arrival": "16:00", "flying_hours": 2.0},
    {"from": "TBU", "to": "AKL", "departure": "15:00", "arrival": "17:00", "flying_hours": 2.0},
    {"from": "APW", "to": "AKL", "departure": "16:00", "arrival": "18:00", "flying_hours": 2.0},
    {"from": "IPC", "to": "SCL", "departure": "17:00", "arrival": "19:00", "flying_hours": 2.0},
] 