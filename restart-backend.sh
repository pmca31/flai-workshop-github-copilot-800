#!/bin/bash

echo "🔄 Restarting OctoFit Tracker Backend..."
echo ""

# Stop any running Django processes
echo "Stopping existing Django processes..."
pkill -f "python.*manage.py runserver" 2>/dev/null || echo "No existing process found"

# Wait a moment
sleep 2

# Start the Django backend
echo "Starting Django backend..."
cd octofit-tracker/backend

# Activate virtual environment and run server
source venv/bin/activate
python manage.py runserver 0.0.0.0:8000 &

echo ""
echo "✅ Backend restarted!"
echo "Backend running on http://localhost:8000"
echo ""
echo "Test the Teams API:"
echo "  curl http://localhost:8000/api/teams/"
