/**
 * API Configuration
 * 
 * Provides a centralized API base URL configuration that works in both
 * local development and GitHub Codespaces environments.
 */

/**
 * Gets the API base URL based on environment configuration.
 * 
 * Priority:
 * 1. REACT_APP_API_BASE_URL - explicit API URL (e.g., "http://localhost:8000")
 * 2. REACT_APP_CODESPACE_NAME - Codespaces environment (builds https://{name}-8000.app.github.dev)
 * 3. Default - falls back to http://localhost:8000
 * 
 * @returns {string} The API base URL without trailing slash
 */
const getApiBaseUrl = () => {
  // Check for explicit API base URL first
  if (process.env.REACT_APP_API_BASE_URL) {
    return process.env.REACT_APP_API_BASE_URL.replace(/\/$/, ''); // Remove trailing slash
  }
  
  // Check if running in GitHub Codespaces
  if (process.env.REACT_APP_CODESPACE_NAME) {
    return `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev`;
  }
  
  // Default to localhost for local development
  return 'http://localhost:8000';
};

export const API_BASE_URL = getApiBaseUrl();

/**
 * Constructs a full API endpoint URL.
 * 
 * @param {string} path - The API endpoint path (e.g., "/api/users/")
 * @returns {string} The complete API URL
 */
export const getApiUrl = (path) => {
  // Ensure path starts with /
  const normalizedPath = path.startsWith('/') ? path : `/${path}`;
  return `${API_BASE_URL}${normalizedPath}`;
};

const apiConfig = {
  API_BASE_URL,
  getApiUrl,
};

export default apiConfig;
