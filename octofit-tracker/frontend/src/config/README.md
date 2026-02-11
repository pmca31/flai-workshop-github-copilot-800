# API Configuration

This directory contains the API configuration for the OctoFit Tracker frontend.

## api.js

The `api.js` file provides a centralized configuration for API endpoints with automatic environment detection.

### Features

- **Automatic Environment Detection**: Detects if running in GitHub Codespaces or local development
- **Localhost Fallback**: Automatically falls back to `http://localhost:8000` when `REACT_APP_CODESPACE_NAME` is not set
- **Single Source of Truth**: All API URLs are generated from this configuration

### Usage

```javascript
import { getApiUrl } from '../config/api';

// Get the full API URL for an endpoint
const apiUrl = getApiUrl('/api/users/');
// Returns: http://localhost:8000/api/users/ (local)
//      or: https://{codespace}-8000.app.github.dev/api/users/ (Codespaces)
```

### Environment Variables

- `REACT_APP_CODESPACE_NAME`: Set this to your GitHub Codespace name when deploying to Codespaces
- Leave empty or unset for local development to use `http://localhost:8000`

### Benefits

1. **No More "undefined" URLs**: Prevents `https://undefined-8000...` errors during local development
2. **Centralized Configuration**: All API URLs are managed in one place
3. **Environment Agnostic**: Works seamlessly in both local and Codespaces environments
4. **Easy Testing**: Simple to test and verify URL generation
