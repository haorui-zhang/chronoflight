import React, { useEffect, useRef, useState } from 'react';
import * as d3 from 'd3';

// Sample flight data
const sampleFlights = [
  {
    id: 'FL001',
    airline: 'Airline A',
    flightNumber: 'AA123',
    departure: {
      city: 'New York',
      airport: 'JFK',
      time: new Date('2024-03-20T10:00:00'),
      coordinates: [-73.7781, 40.6413]
    },
    arrival: {
      city: 'London',
      airport: 'LHR',
      time: new Date('2024-03-20T22:00:00'),
      coordinates: [-0.4543, 51.4700]
    }
  },
  {
    id: 'FL002',
    airline: 'Airline B',
    flightNumber: 'BB456',
    departure: {
      city: 'Tokyo',
      airport: 'NRT',
      time: new Date('2024-03-20T12:00:00'),
      coordinates: [140.3861, 35.7720]
    },
    arrival: {
      city: 'Sydney',
      airport: 'SYD',
      time: new Date('2024-03-20T23:00:00'),
      coordinates: [151.1772, -33.8688]
    }
  }
];

const FlightVisualization = () => {
  const timelineRef = useRef();
  const mapRef = useRef();
  const [currentTime, setCurrentTime] = useState(new Date('2024-03-20T10:00:00'));

  useEffect(() => {
    if (timelineRef.current) {
      drawTimeline();
    }
    if (mapRef.current) {
      drawMap();
    }
  }, [currentTime]);

  const drawTimeline = () => {
    const margin = { top: 20, right: 20, bottom: 30, left: 40 };
    const width = timelineRef.current.clientWidth - margin.left - margin.right;
    const height = timelineRef.current.clientHeight - margin.top - margin.bottom;

    // Clear previous content
    d3.select(timelineRef.current).selectAll('*').remove();

    const svg = d3.select(timelineRef.current)
      .append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

    // Create time scale
    const timeScale = d3.scaleTime()
      .domain([
        new Date('2024-03-20T00:00:00'),
        new Date('2024-03-21T00:00:00')
      ])
      .range([0, width]);

    // Create y scale for flights
    const yScale = d3.scaleLinear()
      .domain([0, sampleFlights.length])
      .range([height, 0]);

    // Add axes
    const xAxis = d3.axisBottom(timeScale);
    const yAxis = d3.axisLeft(yScale);

    svg.append('g')
      .attr('transform', `translate(0,${height})`)
      .call(xAxis);

    svg.append('g')
      .call(yAxis);

    // Add flight lines
    sampleFlights.forEach((flight, i) => {
      svg.append('line')
        .attr('x1', timeScale(flight.departure.time))
        .attr('y1', yScale(i) + 10)
        .attr('x2', timeScale(flight.arrival.time))
        .attr('y2', yScale(i) + 10)
        .attr('stroke', '#2196F3')
        .attr('stroke-width', 2);
    });
  };

  const drawMap = () => {
    const margin = { top: 20, right: 20, bottom: 30, left: 40 };
    const width = mapRef.current.clientWidth - margin.left - margin.right;
    const height = mapRef.current.clientHeight - margin.top - margin.bottom;

    // Clear previous content
    d3.select(mapRef.current).selectAll('*').remove();

    const svg = d3.select(mapRef.current)
      .append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', `translate(${margin.left},${margin.top})`);

    // Create projection
    const projection = d3.geoMercator()
      .scale(100)
      .center([0, 0])
      .translate([width / 2, height / 2]);

    // Draw flight paths
    sampleFlights.forEach(flight => {
      const path = d3.line()
        .x(d => projection(d)[0])
        .y(d => projection(d)[1]);

      svg.append('path')
        .datum([flight.departure.coordinates, flight.arrival.coordinates])
        .attr('fill', 'none')
        .attr('stroke', '#2196F3')
        .attr('stroke-width', 2)
        .attr('d', path);
    });
  };

  return (
    <div className="visualization-container">
      <div className="timeline-container" ref={timelineRef}></div>
      <div className="map-container" ref={mapRef}></div>
      <div className="controls">
        <input
          type="range"
          min="0"
          max="24"
          value={currentTime.getHours()}
          onChange={(e) => {
            const newTime = new Date(currentTime);
            newTime.setHours(parseInt(e.target.value));
            setCurrentTime(newTime);
          }}
        />
        <span>{currentTime.toLocaleTimeString()}</span>
      </div>
    </div>
  );
};

export default FlightVisualization; 