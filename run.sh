#!/bin/bash
# LejTing System Launcher
# Obligatorisk opgave 1 INNT

echo "=== LejTing - Rental Management System ==="
echo "Obligatorisk opgave 1 INNT"
echo ""

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.6"

if python3 -c "import sys; exit(0 if sys.version_info >= (3, 6) else 1)"; then
    echo "Python version $PYTHON_VERSION detected ✓"
else
    echo "Error: Python 3.6 or higher is required. Found: $PYTHON_VERSION"
    exit 1
fi

echo ""
echo "Please select an option:"
echo "1. Run interactive CLI"
echo "2. Run demo with sample data"
echo "3. Run test suite"
echo "4. View help/documentation"
echo ""

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo "Starting interactive CLI..."
        python3 lejting_cli.py
        ;;
    2)
        echo "Running demo with sample data..."
        python3 lejting.py
        ;;
    3)
        echo "Running test suite..."
        python3 test_lejting.py
        ;;
    4)
        echo "Displaying README..."
        if command -v less &> /dev/null; then
            less README.md
        else
            cat README.md
        fi
        ;;
    *)
        echo "Invalid choice. Please run the script again and select 1-4."
        exit 1
        ;;
esac