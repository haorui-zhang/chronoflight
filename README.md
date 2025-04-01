# Flight Reachability Map

An interactive web application that visualizes reachable destinations from any major airport worldwide. The application shows direct flights, one-stop flights, and multi-stop flights with different colors and provides detailed information about flight paths and layovers.

## Features

- Interactive world map visualization
- Real-time flight path display
- Color-coded flight paths:
  - Cyan: Direct flights
  - Blue: One-stop flights
  - Green: Multi-stop flights
- Detailed flight information including:
  - Total flying time
  - Number of hops
  - Layover details
  - Departure and arrival times
- Time slider to explore different flight durations
- Animation feature to visualize flight expansion
- Zoom and pan capabilities
- Mobile-responsive design

## Technology Stack

- Backend: Python/Flask
- Frontend: D3.js for visualization
- Deployment: Render.com

## Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd flight-reachability-map
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Deployment

The application is deployed on Render.com. To deploy your own instance:

1. Create a Render.com account
2. Connect your GitHub repository
3. Create a new Web Service
4. Configure the service:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Deploy!

## License

MIT License 