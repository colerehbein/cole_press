#!/usr/bin/env bash
set -euo pipefail

# Install R
sudo apt-get update
sudo apt-get install -y r-base

# Install Quarto
QUARTO_VERSION="1.7.31"
DEB="quarto-${QUARTO_VERSION}-linux-amd64.deb"
wget -q "https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/${DEB}"
sudo dpkg -i "$DEB"
rm "$DEB"
