/**
 * API Configuration
 * Provides a centralized way to configure the API base URL
 * with automatic fallback to localhost for local development
 */

const getApiBaseUrl = () => {
  // Check if we have a custom API base URL set
  if (process.env.REACT_APP_API_BASE_URL) {
    return process.env.REACT_APP_API_BASE_URL;
  }

  // Check if we're in a GitHub Codespace
  if (process.env.REACT_APP_CODESPACE_NAME) {
    return `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev`;
  }

  // Default to localhost for local development
  return 'http://localhost:8000';
};

export const API_BASE_URL = getApiBaseUrl();

/**
 * Helper function to build API endpoint URLs
 * @param {string} endpoint - The API endpoint path (e.g., '/api/users/')
 * @returns {string} - The full API URL
 */
export const getApiUrl = (endpoint) => {
  // Ensure endpoint starts with /
  const normalizedEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  return `${API_BASE_URL}${normalizedEndpoint}`;
};
