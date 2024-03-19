#!/usr/bin/env bash

# Update your package lists
sudo apt-get update

# Install MySQL 5.7
sudo apt-get install -y mysql-server-5.7

# Check the status of MySQL service
sudo service mysql status

# Check the installed version of MySQL
mysql --version

