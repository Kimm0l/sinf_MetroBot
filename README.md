# Trabajo asignatura SINF de la UPV 

## Metodología

https://schoolofdata.org/methodology/

## Define

Creación de un bot para Telegram donde se puedan planificar las rutas de metro, 
una vez creadas se pueden guardar y crear etiquetas de ellas para su facilidad de uso.

## Find

Web scraping: http://www.metrovalencia.es/planificador.php

## Get

Obtención de la información de salida y destino de las estaciones, duración y linea que coger.
Inluyendo los transbordos.

## Clean

Parsear la información obtenido con el web scraping para que sea lo más concisa y rápida posible.

## Present

Mostrar al usuario la información concisa:

* Estación de salida.
* Línea de metro.
* Transbordos.
* Dirección.
* Duración.

# Instalación

Es necesario tener Python instalado en el sistema.

Se recomienta instalar virtualenv:

`sudo apt-get install virtualenv`

A continuación se activa Virtualenv dentro del dierctorio descargado:

`source bin/activate`

Instalar las dependencias con:

`sudo pip install -r requirements.txt`

Finalmente hay que incluir el token del Bot de telegram como argumento del método Telebot('token') Línea 6.

# Ejecución

Simplemente con:

`python main.py`
