# OctoFit Tracker Frontend

React-based frontend application for the OctoFit Tracker fitness tracking system.

## Features

- **User Management**: View and manage user profiles
- **Activity Tracking**: Log and view fitness activities
- **Team Management**: Create and manage fitness teams
- **Leaderboard**: Competitive rankings based on activity
- **Workout Library**: Browse personalized workout suggestions

## Setup

### Prerequisites

- Node.js and npm installed
- Backend API running on port 8000

### Installation

1. Install dependencies:
   ```bash
   npm install
   ```

2. Configure environment variables:
   ```bash
   # Create .env file with recommended configuration
   echo "REACT_APP_API_BASE_URL=http://localhost:8000" > .env
   
   # Or run the setup script to auto-configure for Codespaces
   chmod +x setup.sh
   ./setup.sh
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The app will be available at `http://localhost:3000` or your Codespace's forwarded port 3000.

## Environment Variables

The application uses a centralized API configuration that supports multiple environments:

### Configuration Priority

1. **REACT_APP_API_BASE_URL** (Recommended): Explicit API base URL
   - Example: `http://localhost:8000`
   - Best for local development and production deployments

2. **REACT_APP_CODESPACE_NAME**: GitHub Codespaces auto-detection
   - Automatically builds: `https://{name}-8000.app.github.dev`
   - Legacy support for existing setups

3. **Default Fallback**: `http://localhost:8000`
   - Used when no environment variables are set
   - Ensures the app works out-of-the-box locally

### Configuration Examples

**Local Development:**
```bash
REACT_APP_API_BASE_URL=http://localhost:8000
```

**GitHub Codespaces (legacy):**
```bash
REACT_APP_CODESPACE_NAME=your-codespace-name
```

**Production:**
```bash
REACT_APP_API_BASE_URL=https://api.octofit.example.com
```

## API Integration

The frontend uses a centralized API configuration located in `src/config/api.js`. This ensures consistent API URL handling across all components.

### API Configuration

```javascript
import { getApiUrl } from './config/api';

// Use the helper function to build API URLs
const apiUrl = getApiUrl('/api/users/');
```

The API base URL is automatically determined based on your environment configuration (see Environment Variables section above).

### API Endpoints

- `/api/users/` - User management
- `/api/activities/` - Activity tracking
- `/api/teams/` - Team management
- `/api/leaderboard/` - Competitive rankings
- `/api/workouts/` - Workout suggestions

## Components

- **Activities**: Display and log fitness activities
- **Leaderboard**: Show competitive rankings
- **Teams**: Manage team memberships and goals
- **Users**: View user profiles and statistics
- **Workouts**: Browse personalized workout recommendations

## Development

```bash
# Start development server
npm start

# Run tests
npm test

# Build for production
npm build

# Run linter
npm run lint
```

## Troubleshooting

### API Connection Issues

If you see CORS errors or connection failures:

1. Ensure the Django backend is running on port 8000
2. Check that CORS is properly configured in Django settings
3. Verify your environment variables are set correctly:
   - For local dev: `REACT_APP_API_BASE_URL=http://localhost:8000`
   - For Codespaces: `REACT_APP_CODESPACE_NAME` should be set
4. Check the browser console for the actual API URL being used
5. Ensure the API base URL is accessible from your browser

### Component Data Not Loading

All components log API endpoints and fetched data to the browser console. Open DevTools (F12) to debug:

```javascript
// Each component logs:
console.log('Fetching from [Component] API endpoint:', apiUrl);
console.log('[Component] data fetched:', data);
```

## Architecture

- **React Router**: Client-side routing for SPA navigation
- **Bootstrap 5**: Responsive UI components and styling
- **Fetch API**: RESTful API communication
- **Environment Variables**: Configuration management

## License

MIT License - See LICENSE file for details
