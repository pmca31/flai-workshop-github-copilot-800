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
   # Run the setup script to auto-configure
   chmod +x setup.sh
   ./setup.sh
   
   # Or manually create .env file
   echo "REACT_APP_CODESPACE_NAME=${CODESPACE_NAME}" > .env
   ```

3. Start the development server:
   ```bash
   npm start
   ```

The app will be available at `http://localhost:3000` or your Codespace's forwarded port 3000.

## Environment Variables

- `REACT_APP_CODESPACE_NAME`: Your GitHub Codespace name (auto-populated in Codespaces)

## API Integration

The frontend connects to the Django REST API backend at:
```
https://${REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/
```

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
3. Verify the `REACT_APP_CODESPACE_NAME` environment variable is set correctly
4. Check browser console for detailed error messages

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
