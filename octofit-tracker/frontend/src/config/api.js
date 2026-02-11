/**
 * API Configuration for OctoFit Tracker
 * 
 * Provides a single source of truth for the API base URL with automatic
 * environment detection and fallback to localhost for local development.
 */

/**
 * Get the API base URL based on the environment
 * @returns {string} The API base URL
 */
export const getApiBaseUrl = () => {
  // Check if REACT_APP_CODESPACE_NAME is set and not empty
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
  
  if (codespaceName && codespaceName.trim() !== '') {
    // Running in GitHub Codespaces
    return `https://${codespaceName}-8000.app.github.dev`;
  }
  
  // Fallback to localhost for local development
  return 'http://localhost:8000';
};

/**
 * Build a full API URL for a specific endpoint
 * @param {string} endpoint - The API endpoint path (e.g., '/api/users/')
 * @returns {string} The full API URL
 */
export const getApiUrl = (endpoint) => {
  const baseUrl = getApiBaseUrl();
  // Ensure endpoint starts with /
  const normalizedEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  return `${baseUrl}${normalizedEndpoint}`;
};

// Export the base URL as a constant for convenience
export const API_BASE_URL = getApiBaseUrl();
