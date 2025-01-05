// src/pages/admin/index.js
import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { Download, Eye, BarChart } from 'lucide-react';

export default function AdminDashboard() {
  const [metrics, setMetrics] = useState({
    pageviews: {},
    downloads: {},
    total: {
      pageviews: 0,
      downloads: 0
    }
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchMetrics();
  }, []);

  const fetchMetrics = async () => {
    try {
      const response = await fetch('/data/metrics.json');
      const data = await response.json();
      setMetrics(data);
    } catch (error) {
      console.error('Error fetching metrics:', error);
    } finally {
      setLoading(false);
    }
  };

  const prepareChartData = () => {
    const dates = new Set([
      ...Object.keys(metrics.pageviews),
      ...Object.keys(metrics.downloads)
    ]);

    return Array.from(dates).sort().map(date => ({
      date,
      pageviews: metrics.pageviews[date] || 0,
      downloads: metrics.downloads[date] || 0
    }));
  };

  const chartData = prepareChartData();

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-xl">Loading...</div>
      </div>
    );
  }

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <h1 className="text-3xl font-bold mb-8">Admin Dashboard</h1>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <div className="p-6 bg-white rounded-lg shadow">
          <div className="flex items-center gap-2 mb-4">
            <Eye className="w-5 h-5" />
            <h2 className="text-xl font-semibold">Total Pageviews</h2>
          </div>
          <div className="text-3xl font-bold">{metrics.total.pageviews}</div>
        </div>
        
        <div className="p-6 bg-white rounded-lg shadow">
          <div className="flex items-center gap-2 mb-4">
            <Download className="w-5 h-5" />
            <h2 className="text-xl font-semibold">Total Downloads</h2>
          </div>
          <div className="text-3xl font-bold">{metrics.total.downloads}</div>
        </div>
      </div>

      <div className="bg-white rounded-lg shadow p-6">
        <div className="flex items-center gap-2 mb-4">
          <BarChart className="w-5 h-5" />
          <h2 className="text-xl font-semibold">Activity Over Time</h2>
        </div>
        <div className="h-96">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="date" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line 
                type="monotone" 
                dataKey="pageviews" 
                stroke="#8884d8" 
                name="Pageviews"
              />
              <Line 
                type="monotone" 
                dataKey="downloads" 
                stroke="#82ca9d" 
                name="Downloads"
              />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      {metrics.lastUpdated && (
        <div className="mt-4 text-sm text-gray-500">
          Last updated: {new Date(metrics.lastUpdated).toLocaleString()}
        </div>
      )}
    </div>
  );
}