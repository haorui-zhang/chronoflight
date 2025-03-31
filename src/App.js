import React from 'react';
import FlightVisualization from './components/FlightVisualization';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Flight Timeline Visualization</h1>
      </header>
      <main>
        <FlightVisualization />
      </main>
    </div>
  );
}

export default App; 