#!/bin/bash
#"""
#ESTE SCRIPT INICIA EL VIRTUAL ENVIROMENT Y CONFIGURA LA BASE DE DATOS EN SU DIRECTORIO TAMBIEN SE ENCUENTRA EL REQUIREMENTS.TXT
#"""
sudo echo "Bienvenido"
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-dev
sudo apt-get install -y postgresql postgresql-contrib
echo "INSTALACION"
sudo apt-get install -y virtualenv
echo "CREACION"
virtualenv -p /usr/bin/python3.6 is2_env

echo "\n\n\nACTIVACION\n\n\n"
source ./is2_env/bin/activate
pip list
pip install -r requirements.txt
cd project-item-management-system
sudo -u postgres psql -c '\x' -c "ALTER USER postgres WITH PASSWORD '12345';"

