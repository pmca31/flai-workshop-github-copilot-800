# API Configuration

This application uses a centralized API configuration system that automatically adapts to different environments.

## How It Works

The API configuration (`src/config/api.js`) determines the backend API URL based on the following priority:

1. **Custom API URL** (highest priority)
   - Set via `REACT_APP_API_BASE_URL` environment variable
   - Example: `REACT_APP_API_BASE_URL=http://localhost:8000`
   - Use this to override the default behavior

2. **GitHub Codespaces**
   - Automatically detected via `REACT_APP_CODESPACE_NAME` environment variable
   - Constructs URL: `https://${REACT_APP_CODESPACE_NAME}-8000.app.github.dev`
   - No manual configuration needed in Codespaces

3. **Local Development** (default fallback)
   - Falls back to `http://localhost:8000`
   - Works out of the box for local development

## Configuration Examples

### Local Development
No configuration needed! The app will automatically use `http://localhost:8000`.

### GitHub Codespaces
The setup script automatically sets `REACT_APP_CODESPACE_NAME` in `.env`:
```bash
REACT_APP_CODESPACE_NAME=your-codespace-name
```

### Custom Backend URL
Create or update `.env` file:
```bash
REACT_APP_API_BASE_URL=http://192.168.1.100:8000
# or
REACT_APP_API_BASE_URL=https://my-backend.example.com
```

## Usage in Components

Import and use the `getApiUrl` helper function:

```javascript
import { getApiUrl } from '../config/api';

// Use in your component
const apiUrl = getApiUrl('/api/users/');
const response = await fetch(apiUrl);
```

## Benefits

- **No more "undefined" URLs**: If environment variables are not set, the app falls back to localhost
- **Centralized configuration**: All API URLs are managed in one place
- **Easy to override**: Set `REACT_APP_API_BASE_URL` to point to any backend
- **Works everywhere**: Local development, Codespaces, production deployments
