// src/app/api/metrics/route.js
import { Octokit } from '@octokit/rest';

const octokit = new Octokit({
  auth: process.env.GITHUB_TOKEN
});

const REPO_OWNER = 'mrlynn'; // Replace with your GitHub username
const REPO_NAME = 'MacFaceSwap';
const METRICS_LABEL = 'metrics';

export async function POST(req) {
  try {
    const { type, data } = await req.json();
    
    // Create an issue with metrics data
    await octokit.issues.create({
      owner: REPO_OWNER,
      repo: REPO_NAME,
      title: `Metrics: ${type} - ${new Date().toISOString()}`,
      body: JSON.stringify(data),
      labels: [METRICS_LABEL, type]
    });

    return new Response(JSON.stringify({ success: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' }
    });
  } catch (error) {
    console.error('Error saving metrics:', error);
    return new Response(JSON.stringify({ error: 'Failed to save metrics' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}