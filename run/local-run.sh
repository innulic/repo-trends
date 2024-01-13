#!/bin/bash

run_application()
{
    python3 -m venv venv
    venv/scripts/activate
    pip install -r requirements.txt
    python3 python-client/api/index.py
}

# Function to check and install Python on macOS/Linux
install_python_unix() {
    if ! command -v python3 &> /dev/null; then
        echo "Python not found. Installing..."
        
        # Check if Homebrew is installed on macOS
        if [[ "$OSTYPE" == "darwin"* ]]; then
            if ! command -v brew &> /dev/null; then
                echo "Homebrew not found. Installing Homebrew..."
                /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            fi
            brew install python
        elif [[ "$OSTYPE" == "linux-gnu" ]]; then
            # Linux package manager command (adjust based on your distribution)
            sudo apt-get install python3
        fi
    else
        echo "Python is already installed."
    fi
}

install_python_windows() {
    if ! command -v python &> /dev/null; then
        echo "Python not found. Installing..."
        Start-Process -Wait -FilePath "ms-windows-store://pdp/?ProductId=9p7qf5lrt38f"
    else
        echo "Python is already installed."
    fi
}

# Function to check if an environment variable is set
check_environment_variable() {
    if [ -z "${!1}" ]; then
        return 1
    else
        return 0
    fi
}

# Function to prompt the user to set an environment variable
set_environment_variable() {
    read -p "Enter the value for $1: " value
    export "$1=$value"
}



install_python_if_needed()
{
        # Main script
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    install_python_windows
elif [[ "$OSTYPE" == "linux-gnu" || "$OSTYPE" == "darwin"* ]]; then
    # Linux
    install_python_unix
else
    echo "Unsupported operating system."
fi
}

set_environment_variable_if_needed()
{
    environment_variable=("SECRET_ID" "CLIENT_ID")
    # Check and set environment variables
    for element in "${environment_variable[@]}"; do
        if ! check_environment_variable $element; then
            set_environment_variable $element
        fi
    done
}

setup_local_environment()
{
    install_python_if_needed
    set_environment_variable_if_needed
}


setup_local_environment
run_application