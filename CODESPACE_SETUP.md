# OctoFit Tracker - Codespace Setup & Testing Guide

## Configuration Summary

The following files have been configured to work with GitHub Codespaces:

### 1. Django Settings ([octofit-tracker/backend/octofit_tracker/settings.py](octofit-tracker/backend/octofit_tracker/settings.py))

- **ALLOWED_HOSTS**: Dynamically configured to include:
  - `localhost`
  - `127.0.0.1`
  - `${CODESPACE_NAME}-8000.app.github.dev` (when running in Codespaces)

- **Proxy Headers**: Configured for GitHub Codespaces HTTPS proxy
  - `USE_X_FORWARDED_HOST = True`
  - `SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')`

### 2. VS Code Launch Configuration ([.vscode/launch.json](.vscode/launch.json))

Pre-configured with:
- **Launch Django Backend**: Runs Django on `0.0.0.0:8000`
- **Launch React Frontend**: Runs React on port `3000`

### 3. Port Forwarding ([.devcontainer/devcontainer.json](.devcontainer/devcontainer.json))

- Port 8000: Django API (public)
- Port 3000: React frontend (public)
- Port 27017: MongoDB (private)

## Starting the Server

### Option 1: Using VS Code Debugger (Recommended)

1. Open the **Run and Debug** panel (Ctrl+Shift+D or Cmd+Shift+D)
2. Select "Launch Django Backend" from the dropdown
3. Click the green play button or press F5

The server will start with debugging enabled.

### Option 2: Using Terminal

```bash
# Activate virtual environment
source octofit-tracker/backend/venv/bin/activate

# Start Django server
cd octofit-tracker/backend
python manage.py runserver 0.0.0.0:8000
```

## API Endpoints

The REST API is available at:

**In GitHub Codespaces:**
```
https://${CODESPACE_NAME}-8000.app.github.dev/api/
```

**Locally:**
```
http://localhost:8000/api/
```

### Available Endpoints

- `/api/users/` - User management
- `/api/teams/` - Team management
- `/api/activities/` - Activity tracking
- `/api/leaderboard/` - Leaderboard entries
- `/api/workouts/` - Workout suggestions

## Testing the API

### Manual Testing with curl

#### Test API Root
```bash
# In Codespaces
curl https://${CODESPACE_NAME}-8000.app.github.dev/api/

# Locally
curl http://localhost:8000/api/
```

#### Test Specific Endpoints
```bash
# Users endpoint
curl https://${CODESPACE_NAME}-8000.app.github.dev/api/users/

# Activities endpoint
curl https://${CODESPACE_NAME}-8000.app.github.dev/api/activities/

# Teams endpoint
curl https://${CODESPACE_NAME}-8000.app.github.dev/api/teams/

# Leaderboard endpoint
curl https://${CODESPACE_NAME}-8000.app.github.dev/api/leaderboard/

# Workouts endpoint
curl https://${CODESPACE_NAME}-8000.app.github.dev/api/workouts/
```

### Automated Testing Script

Run the automated test script:

```bash
chmod +x test_api.sh
./test_api.sh
```

This script will:
1. Detect if running in Codespaces or locally
2. Test all API endpoints
3. Display HTTP status codes
4. Show sample response data

## Verifying Configuration

### Check ALLOWED_HOSTS

```bash
# Display current ALLOWED_HOSTS configuration
cd octofit-tracker/backend
source venv/bin/activate
python -c "import os; os.environ['CODESPACE_NAME'] = os.getenv('CODESPACE_NAME', 'test'); from octofit_tracker import settings; print('ALLOWED_HOSTS:', settings.ALLOWED_HOSTS)"
```

### Check MongoDB Connection

```bash
# Verify MongoDB is running
ps aux | grep mongod | grep -v grep

# Test MongoDB connection
mongosh --eval "db.adminCommand('ping')"
```

## Troubleshooting

### Server Not Starting

1. Check if MongoDB is running: `ps aux | grep mongod`
2. Check if port 8000 is already in use: `lsof -i :8000`
3. Check Python virtual environment: `which python` (should show venv path)

### CORS Errors

The Django backend is configured with `CORS_ALLOW_ALL_ORIGINS = True` for development.

### Connection Refused

1. Verify the server is running on `0.0.0.0:8000` not `127.0.0.1:8000`
2. Check port forwarding in VS Code (Ports tab in terminal panel)
3. Ensure CODESPACE_NAME environment variable is set: `echo $CODESPACE_NAME`

### 400 Bad Request or Invalid Host Header

This means ALLOWED_HOSTS is not configured correctly. Verify:
```bash
echo $CODESPACE_NAME
# Should output your codespace name
```

The settings should automatically add `${CODESPACE_NAME}-8000.app.github.dev` to ALLOWED_HOSTS.

## Next Steps

1. ✅ Start the Django backend
2. ✅ Test API endpoints with curl
3. Configure and start the React frontend
4. Test end-to-end functionality

## Additional Resources

- [Django Settings Documentation](https://docs.djangoproject.com/en/4.1/ref/settings/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [GitHub Codespaces Port Forwarding](https://docs.github.com/en/codespaces/developing-in-codespaces/forwarding-ports-in-your-codespace)
