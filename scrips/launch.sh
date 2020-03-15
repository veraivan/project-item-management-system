#!/bin/bash
sudo echo "Hola"
git clone https://github.com/veraivan/project-item-management-system.git
sudo apt-get install python3-pip
sudo apt-get install python3-dev
sudo apt-get install postgresql postgresql-contrib
echo "INSTALACION"
sudo apt-get install virtualenv
echo "CREACIONN"
virtualenv -p /usr/bin/python3.6 is2_env

echo "\n\n\nACTIVACION\n\n\n"
#ln -s is2_env/bin/activate
source ./is2_env/bin/activate
pip list
pip install -r requirements.txt
pip list
cd project-item-management-system
git checkout desarrolloPruebaGiuli
sudo -u postgres psql -c '\x' -c "ALTER USER postgres WITH PASSWORD '12345';"


deactivate
#rm -rf is2_env/

