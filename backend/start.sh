#!/bin/bash

echo "🎁 Gift Recommendation System - Backend Startup"
echo "=============================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "🚀 Starting FastAPI server..."
echo "📍 Server will run at: http://localhost:4000"
echo "📖 API docs available at: http://localhost:4000/docs"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Start the server
python main.py
