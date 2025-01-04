// src/hooks/useAnalytics.js
import { useEffect, useCallback } from 'react';

const STORAGE_KEY = 'macfaceswap_metrics';

export const useAnalytics = () => {
  const trackPageView = useCallback(() => {
    const pageData = {
      timestamp: new Date().toISOString(),
      path: window.location.pathname,
      referrer: document.referrer || 'direct',
      userAgent: navigator.userAgent
    };
    
    saveMetric('pageview', pageData);
  }, []);

  const trackDownload = useCallback((version) => {
    const downloadData = {
      timestamp: new Date().toISOString(),
      version,
      referrer: document.referrer || 'direct'
    };
    
    saveMetric('download', downloadData);
  }, []);

  const saveMetric = (type, data) => {
    try {
      const metrics = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
      if (!metrics[type]) metrics[type] = [];
      metrics[type].push(data);
      localStorage.setItem(STORAGE_KEY, JSON.stringify(metrics));
      
      // You could also send to a server endpoint here
      // fetch('/api/metrics', {
      //   method: 'POST',
      //   body: JSON.stringify({ type, data })
      // });
    } catch (error) {
      console.error('Error saving metrics:', error);
    }
  };

  useEffect(() => {
    // Track page view on mount
    trackPageView();
  }, [trackPageView]);

  return {
    trackDownload,
    trackPageView
  };
};