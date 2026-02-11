#!/bin/bash

# Setup script for OctoFit Tracker Frontend
# This script configures the environment variables and logo files needed for the React app

echo "🚀 Setting up OctoFit Tracker Frontend..."
echo ""

# Navigate to frontend directory
cd "$(dirname "$0")"

# Create .env file with Codespace name
if [ -n "$CODESPACE_NAME" ]; then
    echo "REACT_APP_CODESPACE_NAME=$CODESPACE_NAME" > .env
    echo "✓ .env file created with CODESPACE_NAME: $CODESPACE_NAME"
else
    echo "⚠ Warning: CODESPACE_NAME environment variable not found"
    echo "Please set REACT_APP_CODESPACE_NAME manually in .env file"
fi

# Copy OctoFit logo files
echo ""
echo "📸 Copying OctoFit logo files..."

if [ -f "../../docs/octofitapp-small.png" ]; then
    cp ../../docs/octofitapp-small.png public/octofitapp-small.png
    cp ../../docs/octofitapp-small.png public/favicon.ico
    cp ../../docs/octofitapp-small.png src/octofitapp-small.png
    echo "✓ Logo files copied successfully!"
else
    echo "⚠ Warning: Logo file not found at ../../docs/octofitapp-small.png"
    echo "Please ensure the logo file exists or update the path"
fi

# Display the current configuration
echo ""
echo "📋 Current configuration:"
if [ -f ".env" ]; then
    cat .env
fi

echo ""
echo "✨ Setup complete! You can now run:"
echo "  npm start    - Start the development server on port 3000"
echo "  npm build    - Build for production"
echo "  npm test     - Run tests"
echo ""
echo "🎨 The app features:"
echo "  • Modern gradient design with vibrant colors"
echo "  • OctoFit logo in navbar and as favicon"
echo "  • Bootstrap-styled tables and components"
echo "  • Responsive mobile-friendly layout"
