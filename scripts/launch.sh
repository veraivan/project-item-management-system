#!/bin/bash
sudo echo "Bienvenido"
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-dev
sudo apt-get install -y postgresql postgresql-contrib
sudo apt-get install postgresql
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev
echo "INSTALACION"
sudo apt-get install -y virtualenv
echo "CREACION"
virtualenv -p /usr/bin/python3.6 is2_env

echo "\n\n\nACTIVACION\n\n\n"
source ./is2_env/bin/activate
pip list
pip install -r requirements.txt
cd project-item-management-system
echo "Se crea la base de datos"
sudo -u postgres psql -c 'create database db_proyecto;'
sudo -u postgres psql -c '\x' -c "ALTER USER postgres WITH PASSWORD 'postgres';"