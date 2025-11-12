#!/bin/bash

# Fuzzy System - Start Script
# This script starts both backend and frontend using Podman Compose

set -e  # Exit on error

echo "=================================================="
echo "  🚀 Starting Fuzzy System with Podman"
echo "=================================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if podman is installed
if ! command -v podman &> /dev/null; then
    echo -e "${RED}❌ Error: Podman is not installed${NC}"
    echo "Please install Podman first:"
    echo "  brew install podman"
    exit 1
fi

# Check if podman-compose is installed
if ! command -v podman-compose &> /dev/null; then
    echo -e "${YELLOW}⚠️  Warning: podman-compose is not installed${NC}"
    echo "Installing podman-compose..."
    pip3 install podman-compose
fi

# Initialize podman machine if not running (macOS specific)
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo -e "${YELLOW}📦 Checking Podman machine status...${NC}"
    if ! podman machine list | grep -q "Currently running"; then
        echo "Starting Podman machine..."
        podman machine start || {
            echo -e "${YELLOW}Creating new Podman machine...${NC}"
            podman machine init
            podman machine start
        }
    fi
    echo -e "${GREEN}✓ Podman machine is running${NC}"
    echo ""
fi

# Stop any running containers
echo -e "${YELLOW}🛑 Stopping existing containers...${NC}"
podman-compose down 2>/dev/null || true
echo ""

# Build and start containers
echo -e "${YELLOW}🔨 Building containers...${NC}"
podman-compose build

echo ""
echo -e "${YELLOW}🚀 Starting containers...${NC}"
podman-compose up -d

echo ""
echo -e "${GREEN}✓ Containers started successfully!${NC}"
echo ""
echo "=================================================="
echo "  📊 Service URLs:"
echo "=================================================="
echo -e "  Frontend:  ${GREEN}http://localhost:5173${NC}"
echo -e "  Backend:   ${GREEN}http://localhost:8000${NC}"
echo -e "  API Docs:  ${GREEN}http://localhost:8000/docs${NC}"
echo "=================================================="
echo ""
echo "Commands:"
echo "  View logs:     podman-compose logs -f"
echo "  Stop services: podman-compose down"
echo "  Restart:       podman-compose restart"
echo ""
echo -e "${GREEN}Happy coding! 🎉${NC}"
