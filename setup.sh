#!/usr/bin/env bash

set -e
apt-get update
apt-get install -y r-base
curl -L -o quarto.deb https://github.com/quarto-dev/quarto-cli/releases/download/v1.7.31/quarto-1.7.31-linux-amd64.deb
apt-get install -y ./quarto.deb
rm quarto.deb

