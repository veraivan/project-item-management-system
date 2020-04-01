#!/bin/bash
sudo echo "Hola"
sudo apt-get install python3-pip
sudo apt-get install python3-dev
sudo apt-get install libpq-dev
sudo apt-get install postgresql postgresql-contrib
sudo echo "Bienvenido"

echo "INSTALACION"
sudo apt-get install virtualenv
echo "CREACIONN"
virtualenv -p /usr/bin/python3.6 is2_env

echo "\n\n\nACTIVACION\n\n\n"
source is2_env/bin/activate
pip install -r requirements.txt

echo "Se crea la base de datos"
sudo -u postgres psql -c 'create database db_proyecto;'
sudo -u postgres psql -c '\x' -c "ALTER USER postgres WITH PASSWORD 'postgres';"