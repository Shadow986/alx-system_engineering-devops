#!/usr/bin/env bash
# This script installs MySQL 5.7, creates a user, and checks the user's permissions

# Update your package lists
sudo apt-get update

# Install MySQL 5.7
sudo apt-get install -y mysql-server-5.7

# Create a MySQL user named holberton_user with the host name set to localhost and the password projectcorrection280hbtn
mysql -u root -e "CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';"

# Grant replication client permissions to holberton_user
mysql -u root -e "GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';"

# Check the status of MySQL service
sudo service mysql status

# Check the installed version of MySQL
mysql --version

# Check the permissions of holberton_user
mysql -uholberton_user -pprojectcorrection280hbtn -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"

