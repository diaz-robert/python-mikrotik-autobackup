# Script to Backup Mikrotik

This Python script uses the `paramiko` library to connect to multiple Mikrotik devices and backup their configurations into an `.rsc` file.

## Requirements

- Python 3.x
- `paramiko` library

## Installation

1. Clone the repository: `git clone https://github.com/diaz-robert/python-mikrotik-autobackup.git`
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

The `devices.txt` file contains the information of the devices in the following format:

```
# This is a comment and will not be processed
Description, IP, username, certificate, port
```

The fields are:

- `Description`: A description of the device.
- `IP`: The IP address of the device.
- `username`: The username to connect to the device.
- `certificate`: The path of the file with the certificate.
- `port`: The port to connect to the device.

Example:

```
Office Router,192.168.1.1,admin,~/certificate.pem,22
Home Router,192.168.2.1,admin,~/certificate.pem,22
```

To generate an authentication certificate for the Mikrotik user, follow the steps described in the official Mikrotik documentation: https://wiki.mikrotik.com/wiki/OpenVPN_Certificates#Creating_user_certificates_using_the_easy-rsa_scripts.

## Usage

Execute the script with the following command:

```
python backup.py
```

The script will create an `.rsc` file with the backup of each device in a subdirectory with the name of the device description. If the subdirectory does not exist, the script will create it automatically.

## Contribution

If you find any errors or wish to add functionality, please open a pull request.

---
# Script para hacer respaldo de Mikrotik

Este script en Python utiliza la librería `paramiko` para conectarse a múltiples dispositivos Mikrotik y hacer respaldo de la configuración en un archivo `.rsc`.

## Requisitos

- Python 3.x
- Librería `paramiko`

## Instalación

1. Clonar el repositorio: `git clone https://github.com/diaz-robert/python-mikrotik-autobackup.git`
2. Instalar las dependencias:
   ```
   pip install -r requirements.txt
   ```

## Configuración

El archivo `devices.txt` contiene la información de los dispositivos en el siguiente formato:

```
# Este es un comentario y no se procesará
Descripción, IP, usuario, certificado, puerto
```

Los campos son:

- `Descripción`: Una descripción del dispositivo.
- `IP`: La dirección IP del dispositivo.
- `usuario`: El nombre de usuario para conectarse al dispositivo.
- `certificado`: La ruta del archivo con el certificado.
- `puerto`: El puerto para conectarse al dispositivo.

Ejemplo:

```
Router de la oficina,192.168.1.1,admin,~/certificado.pem,22
Router de la casa,192.168.2.1,admin,~/certificado.pem,22
```

Para generar un certificado de autenticación para el usuario del Mikrotik, siga los pasos descritos en la documentación oficial de Mikrotik: https://wiki.mikrotik.com/wiki/OpenVPN_Certificates#Creating_user_certificates_using_the_easy-rsa_scripts.

## Uso

Ejecute el script con el siguiente comando:

```
python respaldo.py
```

El script creará un archivo `.rsc` con el respaldo de cada dispositivo en un subdirectorio con el nombre de la descripción del dispositivo. Si el subdirectorio no existe, el script lo creará automáticamente.

## Contribución

Si encuentra algún error o desea agregar una funcionalidad, por favor abra un pull request.