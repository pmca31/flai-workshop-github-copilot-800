/**
 * API Configuration
 * 
 * Provides a centralized API base URL configuration that works in both
 * GitHub Codespaces and local development environments.
 * 
 * In Codespaces: Uses the REACT_APP_API_BASE_URL if set, or constructs
 *                the URL from REACT_APP_CODESPACE_NAME
 * Locally: Defaults to http://localhost:8000
 */

const getApiBaseUrl = () => {
  // First, check if a direct API base URL is provided
  if (process.env.REACT_APP_API_BASE_URL) {
    return process.env.REACT_APP_API_BASE_URL;
  }
  
  // Second, check if we're in a Codespace and construct the URL
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
  if (codespaceName && codespaceName !== 'undefined') {
    return `https://${codespaceName}-8000.app.github.dev`;
  }
  
  // Default to localhost for local development
  return 'http://localhost:8000';
};

export const API_BASE_URL = getApiBaseUrl();

// Helper function to construct full API URLs
export const getApiUrl = (endpoint) => {
  // Ensure endpoint starts with /
  const normalizedEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  return `${API_BASE_URL}${normalizedEndpoint}`;
};
