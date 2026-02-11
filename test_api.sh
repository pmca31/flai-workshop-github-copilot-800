#!/bin/bash

# Test script for OctoFit Tracker API

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}=== OctoFit Tracker API Test ===${NC}\n"

# Get the codespace name
CODESPACE_NAME=${CODESPACE_NAME:-"localhost"}

if [ "$CODESPACE_NAME" != "localhost" ]; then
    BASE_URL="https://${CODESPACE_NAME}-8000.app.github.dev"
    echo -e "${GREEN}Running in GitHub Codespaces${NC}"
else
    BASE_URL="http://localhost:8000"
    echo -e "${GREEN}Running locally${NC}"
fi

echo -e "Base URL: ${YELLOW}${BASE_URL}${NC}\n"

# Test API endpoints
echo -e "${YELLOW}Testing API endpoints:${NC}\n"

endpoints=("api/users/" "api/teams/" "api/activities/" "api/leaderboard/" "api/workouts/")

for endpoint in "${endpoints[@]}"; do
    echo -e "Testing ${GREEN}${BASE_URL}/${endpoint}${NC}"
    HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" "${BASE_URL}/${endpoint}")
    
    if [ "$HTTP_CODE" == "200" ]; then
        echo -e "  ✓ Status: ${GREEN}${HTTP_CODE}${NC}"
        # Show first few items
        curl -s "${BASE_URL}/${endpoint}" | python3 -m json.tool | head -20
    else
        echo -e "  ✗ Status: ${RED}${HTTP_CODE}${NC}"
    fi
    echo ""
done

echo -e "\n${YELLOW}=== Test Complete ===${NC}"
