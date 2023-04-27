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
Description, IP, username, port
```

The fields are:

- `Description`: A description of the device.
- `IP`: The IP address of the device.
- `username`: The username to connect to the device.
- `port`: The port to connect to the device.

Example:

```
Office Router,192.168.1.1,admin,22
Home Router,192.168.2.1,admin,22
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
