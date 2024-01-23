#!/bin/bash

# Function to check and update Homebrew
update_homebrew() {
    echo "Checking for Homebrew updates..."
    if command -v brew &> /dev/null; then
        brew update
        brew_outdated=$(brew outdated)

        if [ -n "$brew_outdated" ]; then
            echo "Updating Homebrew packages..."
            brew upgrade
            brew cleanup
            UPDATE_FLAG=true
        else
            echo "No Homebrew updates available."
        fi
    else
        echo "Homebrew not found. Please install Homebrew to use this update script."
    fi
}

# Function to check and update macOS system software
update_macos() {
    echo "Checking for macOS system updates..."
    macos_updates=$(softwareupdate -l)

    if [ -n "$macos_updates" ]; then
        echo "Updating macOS system software..."
        sudo softwareupdate -ia
        UPDATE_FLAG=true
    else
        echo "No macOS system updates available."
    fi
}

# Function to check and update Ruby gems
update_ruby_gems() {
    echo "Updating Ruby gems..."
    gem update --system
    gem cleanup
    UPDATE_FLAG=true
}

# Function to check and update npm and global packages
update_npm() {
    echo "Updating npm and global packages..."
    npm update -g
    npm cache clean -f
    UPDATE_FLAG=true
}

# Function to check and update pip and Python packages
update_pip() {
    echo "Updating pip and Python packages..."
    pip3 install --upgrade pip
    pip3_outdated=$(pip3 list --outdated --format=freeze)

    if [ -n "$pip3_outdated" ]; then
        pip3 freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip3 install -U
        pip3 autoremove -y
        UPDATE_FLAG=true
    else
        echo "No Python package updates available."
    fi
}

UPDATE_FLAG=false

# Run update functions
update_homebrew
update_macos
update_ruby_gems
update_npm
update_pip

if [ "$UPDATE_FLAG" = true ]; then
    echo "All updates and cleanup completed successfully."
else
    echo "No updates or cleanup performed."
fi
