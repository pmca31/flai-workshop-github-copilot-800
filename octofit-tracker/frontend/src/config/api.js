/**
 * API Configuration
 * 
 * Provides a centralized API base URL configuration with environment-aware fallbacks.
 * 
 * Priority:
 * 1. REACT_APP_API_BASE_URL - explicit API base URL override
 * 2. REACT_APP_CODESPACE_NAME - GitHub Codespaces environment
 * 3. http://localhost:8000 - local development fallback
 */

const getApiBaseUrl = () => {
  // Check for explicit API base URL
  if (process.env.REACT_APP_API_BASE_URL) {
    return process.env.REACT_APP_API_BASE_URL;
  }
  
  // Check for GitHub Codespaces environment
  if (process.env.REACT_APP_CODESPACE_NAME) {
    return `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev`;
  }
  
  // Default to localhost for local development
  return 'http://localhost:8000';
};

// Note: API_BASE_URL is computed at module load time based on environment variables.
// In normal React applications, environment variables are set at build time and don't
// change during runtime, so this is the expected behavior. If you need to reconfigure
// the API URL at runtime (e.g., in tests), you'll need to reload the module.
export const API_BASE_URL = getApiBaseUrl();

// Helper function to build API endpoint URLs
export const getApiUrl = (endpoint) => {
  // Ensure endpoint starts with /
  const cleanEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  return `${API_BASE_URL}${cleanEndpoint}`;
};

export default { API_BASE_URL, getApiUrl };
