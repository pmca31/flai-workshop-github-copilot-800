#!/bin/bash

# Test script to check Teams API and member counts

BASE_URL="http://localhost:8000"

echo "🧪 Testing OctoFit Tracker API..."
echo ""

echo "1️⃣ Testing Teams endpoint:"
echo "GET ${BASE_URL}/api/teams/"
echo ""
curl -s "${BASE_URL}/api/teams/" | python3 -m json.tool || echo "Failed to fetch teams"

echo ""
echo ""
echo "2️⃣ Testing Users endpoint:"
echo "GET ${BASE_URL}/api/users/"
echo ""
curl -s "${BASE_URL}/api/users/" | python3 -m json.tool || echo "Failed to fetch users"

echo ""
echo ""
echo "✅ API Test Complete"
echo "Check if member_count appears in team objects above"
