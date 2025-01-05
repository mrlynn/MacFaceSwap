'use client';

import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const AdminDashboard = () => {
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/data/metrics.json')
      .then(res => res.json())
      .then(data => {
        setMetrics(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error loading metrics:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="p-8">Loading metrics...</div>;
  }

  if (!metrics) {
    return <div className="p-8">No metrics available</div>;
  }

  // Convert metrics to chart data
  const chartData = Object.entries(metrics.pageviews).map(([date, views]) => ({
    date,
    views,
    downloads: metrics.downloads[date] || 0
  }));

  return (
    <div className="p-8 bg-gray-50 min-h-screen">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-3xl font-bold mb-8">Analytics Dashboard</h1>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-semibold mb-4">Total Page Views</h2>
            <p className="text-4xl font-bold">{metrics.total.pageviews}</p>
          </div>
          
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-semibold mb-4">Total Downloads</h2>
            <p className="text-4xl font-bold">{metrics.total.downloads}</p>
          </div>
        </div>

        <div className="bg-white p-6 rounded-lg shadow mb-8">
          <h2 className="text-xl font-semibold mb-4">Activity Over Time</h2>
          <div className="h-96">
            <BarChart width={800} height={400} data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="views" fill="#8884d8" name="Page Views" />
              <Bar dataKey="downloads" fill="#82ca9d" name="Downloads" />
            </BarChart>
          </div>
        </div>

        <div className="text-sm text-gray-500">
          Last updated: {new Date(metrics.lastUpdated).toLocaleString()}
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;