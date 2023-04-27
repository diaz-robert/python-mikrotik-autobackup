import paramiko
import time
import os
import sys
from datetime import datetime

# Read device information from 'devices.txt' file
with open('devices.txt', 'r') as f:
    devices = f.readlines()

# Iterate over the devices
for device in devices:
    # If the line starts with '#' it is considered a comment and is not processed
    if device.startswith('#'):
        continue

    # Parse device information
    description, host, user, password, port = device.strip().split(',')
    print(f"Connecting to {host}:{port}...")

    # Create an SSH connection
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=host, username=user, password=password, port=int(port))
        print(f"Connected to {host}:{port}.")

        # Execute 'export' command on Mikrotik
        stdin, stdout, stderr = client.exec_command('export')
        output = stdout.read().decode()

        # Save the generated file in the current directory
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        if not os.path.exists(description):
            os.makedirs(description)
        backup_filename = f"{description}/{description}_{timestamp}.rsc"
        with open(backup_filename, 'w') as f:
            f.write(output)
        print(f"Backup generated successfully on {host}:{port}.")

        # Close the SSH connection
        client.close()
        print(f"Connection closed to {host}:{port}.")

    except Exception as e:
        print(f"Error connecting to {host}:{port}: {e}")
        continue
