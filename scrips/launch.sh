#!/bin/bash
chmod 755 launch


sudo echo "Entrando como Superusuario"

echo "INSTALACION DE PROGRAMAS NECESARIOS"
sudo apt-get update

echo "INSTALACION DE PIP"
sudo apt-get install python3-pip

echo "INSTALACION DE VIRTUALENV"
pip3 install virtualenv


echo "INSTALACION DE POSTGRES"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get install postgresql


echo "INSTALL APACHE"
sudo apt-get install apache2


echo "INSTALACION GIT"
sudo apt-get install git


echo "INSTALACION DE LA LIBRERIA PARA APACHE"
sudo apt-get install libapache2-mod-wsgi-py3

echo "EN PRODUCCIÓN"
echo "#########################################################
# HERRAMIENTAS UTILIZADAS				#
# 	- PYTHON 3.6.9					#
# 	- POSTGRES 12.2				#
#	- DJANGO 3.0.3					#
#	- PIP 19.0.3 					#
#	- PSYCOPG2 2.7.7  				#
#	- APACHE/2.4.29					#
#########################################################"
#VARIABLES
nombre_carpeta="is2-produccion"
nombre_proyecto="project-item-management-system"
usuario="giuli"
nombre_entorno="is2-venv"
dir_inicio="../"
dir_produccion="$dir_inicio/is2-produccion"
dir_entorno="$dir_inicio/$nombre_entorno"
nombre_bd="bd_produccion"
repositorio="https://github.com/veraivan/project-item-management-system.git"
version="v1.0"


echo "CREACION DE LA CAPPETA DE PRODUCCION"
mkdir ../$nombre_carpeta
chmod -R 777 ../$nombre_carpeta
cd ../$nombre_carpeta


echo "CREACION DE LA CARPETA QUE TENDRA EL PROYECTO EN PRODUCCION"
cd $dir_inicio


echo "CREACION DEL ENTORNO VIRTUAL"
virtualenv --python=python3 $nombre_entorno

echo "ACTIVACION DEL ENTORNO"
source $nombre_entorno/bin/activate