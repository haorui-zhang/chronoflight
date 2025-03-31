# Flight Reachability Map

An interactive visualization tool that shows reachable destinations from a starting airport based on flying time. Built with Flask and D3.js.

## Features

- Interactive world map showing reachable destinations
- Time slider to adjust the maximum flying time (0-48 hours)
- Visual representation of flight paths with intermediate stops
- Detailed tooltips showing flight information and layovers
- Real-time updates as you adjust the flying time

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/flight-reachability-map.git
cd flight-reachability-map
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Use the time slider to adjust the maximum flying time
2. Hover over destinations to see detailed flight information
3. Green dots indicate reachable destinations
4. Gray dots indicate unreachable destinations
5. Gold dots show intermediate stops/layovers

## Technologies Used

- Python/Flask for the backend
- D3.js for data visualization
- TopoJSON for map data
- HTML5/CSS3 for the frontend

## License

MIT License 