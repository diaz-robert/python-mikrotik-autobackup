import paramiko
import time
import os
import sys
from datetime import datetime

# Lee la información de los dispositivos desde el archivo 'devices.txt'
with open('devices.txt', 'r') as f:
    devices = f.readlines()

# Itera sobre los dispositivos
for device in devices:
    # si la línea comienza con el carácter # se considera comentario y no es procesado
    if device.startswith('#'):
        continue

    description, host, user, password, port = device.strip().split(',')
    print(f"Conectando a {host}:{port}...")

    # Crea una conexión SSH
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password, port=int(port))
        print(f"Conexión establecida con {host}:{port}.")

        # Ejecuta el comando 'export' en el Mikrotik
        stdin, stdout, stderr = client.exec_command('export')
        output = stdout.read().decode()

        # Guarda el archivo generado en el directorio actual
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        if not os.path.exists(description):
            os.makedirs(description)
        backup_filename = f"{description}/{description}_{timestamp}.rsc"
        with open(backup_filename, 'w') as f:
            f.write(output)
        print(f"Respaldo generado exitosamente en {host}:{port}.")

        # Cierra la conexión SSH
        client.close()
        print(f"Conexión cerrada con {host}:{port}.")

    except Exception as e:
        print(f"Error al conectar a {host}:{port}: {e}")
        continue
