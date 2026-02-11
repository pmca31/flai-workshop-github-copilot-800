#!/bin/bash

# Copy OctoFit logo for use in the frontend
echo "Copying OctoFit logo files..."

# Copy to public directory for favicon
cp ../../docs/octofitapp-small.png public/octofitapp-small.png
cp ../../docs/octofitapp-small.png public/favicon.ico
cp ../../docs/octofitapp-small.png public/logo192.png
cp ../../docs/octofitapp-small.png public/logo512.png

# Copy to src directory for navbar
cp ../../docs/octofitapp-small.png src/octofitapp-small.png

echo "✓ Logo files copied successfully!"
echo "Files created:"
echo "  - public/octofitapp-small.png"
echo "  - public/favicon.ico" 
echo "  - src/octofitapp-small.png"
