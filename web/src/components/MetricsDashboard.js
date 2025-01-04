import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const MetricsDashboard = () => {
  const [metrics, setMetrics] = useState({
    pageviews: [],
    downloads: [],
    events: []
  });

  useEffect(() => {
    // Load metrics from localStorage
    const storedMetrics = JSON.parse(localStorage.getItem('site_metrics') || '{}');
    setMetrics(storedMetrics);

    // Update metrics every minute
    const interval = setInterval(() => {
      const updatedMetrics = JSON.parse(localStorage.getItem('site_metrics') || '{}');
      setMetrics(updatedMetrics);
    }, 60000);

    return () => clearInterval(interval);
  }, []);

  // Process pageview data for chart
  const pageviewData = Object.entries(
    metrics.pageview?.reduce((acc, view) => {
      const date = new Date(view.timestamp).toLocaleDateString();
      acc[date] = (acc[date] || 0) + 1;
      return acc;
    }, {}) || {}
  ).map(([date, count]) => ({ date, views: count }));

  return (
    <div className="p-4 space-y-6">
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-bold mb-4">Site Analytics</h2>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          <div className="bg-blue-50 p-4 rounded-lg">
            <h3 className="text-lg font-semibold">Total Pageviews</h3>
            <p className="text-3xl font-bold">{metrics.pageview?.length || 0}</p>
          </div>
          
          <div className="bg-green-50 p-4 rounded-lg">
            <h3 className="text-lg font-semibold">Total Downloads</h3>
            <p className="text-3xl font-bold">{metrics.download?.length || 0}</p>
          </div>
          
          <div className="bg-purple-50 p-4 rounded-lg">
            <h3 className="text-lg font-semibold">Unique Visitors</h3>
            <p className="text-3xl font-bold">
              {new Set(metrics.pageview?.map(p => p.userAgent)).size || 0}
            </p>
          </div>
        </div>

        <div className="h-64">
          <h3 className="text-lg font-semibold mb-4">Pageviews Over Time</h3>
          <BarChart width={600} height={200} data={pageviewData}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="views" fill="#3b82f6" />
          </BarChart>
        </div>
      </div>
    </div>
  );
};

export default MetricsDashboard;