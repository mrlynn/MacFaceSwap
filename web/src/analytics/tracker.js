// src/analytics/tracker.js

// Initialize the analytics tracker
const initializeAnalytics = () => {
    // Create a unique session ID
    const sessionId = crypto.randomUUID();
    
    // Basic pageview tracking
    trackPageView();
    
    // Attach download tracking to DMG links
    attachDownloadTracking();
    
    return {
      trackEvent,
      trackPageView,
      getSessionMetrics
    };
  };
  
  // Track page views
  const trackPageView = () => {
    const pageData = {
      timestamp: new Date().toISOString(),
      path: window.location.pathname,
      referrer: document.referrer || 'direct',
      userAgent: navigator.userAgent,
      screenResolution: `${window.screen.width}x${window.screen.height}`,
      language: navigator.language
    };
    
    // Send to your backend or local storage
    saveMetric('pageview', pageData);
  };
  
  // Track DMG downloads
  const attachDownloadTracking = () => {
    document.querySelectorAll('a[href$=".dmg"]').forEach(link => {
      link.addEventListener('click', (e) => {
        const downloadData = {
          timestamp: new Date().toISOString(),
          fileName: link.getAttribute('href').split('/').pop(),
          referrer: document.referrer || 'direct'
        };
        
        saveMetric('download', downloadData);
      });
    });
  };
  
  // Generic event tracking
  const trackEvent = (eventName, eventData) => {
    const data = {
      timestamp: new Date().toISOString(),
      event: eventName,
      ...eventData
    };
    
    saveMetric('event', data);
  };
  
  // Save metrics to localStorage (can be replaced with server endpoint)
  const saveMetric = (type, data) => {
    const metrics = JSON.parse(localStorage.getItem('site_metrics') || '{}');
    if (!metrics[type]) metrics[type] = [];
    metrics[type].push(data);
    localStorage.setItem('site_metrics', JSON.stringify(metrics));
    
    // Optional: Send to backend
    if (process.env.METRICS_ENDPOINT) {
      fetch(process.env.METRICS_ENDPOINT, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          type,
          data
        })
      }).catch(console.error); // Silent fail if endpoint unavailable
    }
  };
  
  // Get current session metrics
  const getSessionMetrics = () => {
    return JSON.parse(localStorage.getItem('site_metrics') || '{}');
  };
  
  export default initializeAnalytics;