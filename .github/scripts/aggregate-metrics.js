// .github/scripts/aggregate-metrics.js
const { Octokit } = require('@octokit/rest');
const fs = require('fs');
const path = require('path');

const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN
});

const REPO_OWNER = 'mrlynn'; // Replace with your GitHub username
const REPO_NAME = 'MacFaceSwap';
const METRICS_LABEL = 'metrics';

async function aggregateMetrics() {
  try {
    // Get all issues with metrics label
    const { data: issues } = await octokit.issues.listForRepo({
      owner: REPO_OWNER,
      repo: REPO_NAME,
      labels: METRICS_LABEL,
      state: 'all',
      per_page: 100
    });

    // Process metrics
    const metrics = {
      pageviews: {},
      downloads: {},
      total: {
        pageviews: 0,
        downloads: 0
      },
      lastUpdated: new Date().toISOString()
    };

    issues.forEach(issue => {
      try {
        const data = JSON.parse(issue.body);
        const date = new Date(data.timestamp).toISOString().split('T')[0];
        
        if (issue.labels.find(l => l.name === 'pageview')) {
          metrics.pageviews[date] = (metrics.pageviews[date] || 0) + 1;
          metrics.total.pageviews++;
        }
        
        if (issue.labels.find(l => l.name === 'download')) {
          metrics.downloads[date] = (metrics.downloads[date] || 0) + 1;
          metrics.total.downloads++;
        }
      } catch (e) {
        console.error('Error processing issue:', issue.number, e);
      }
    });

    // Ensure data directory exists
    const dataDir = path.join(process.cwd(), 'data');
    if (!fs.existsSync(dataDir)) {
      fs.mkdirSync(dataDir);
    }

    // Write aggregated metrics
    fs.writeFileSync(
      path.join(dataDir, 'metrics.json'),
      JSON.stringify(metrics, null, 2)
    );

    console.log('Metrics aggregated successfully');
  } catch (error) {
    console.error('Error aggregating metrics:', error);
    process.exit(1);
  }
}

aggregateMetrics();