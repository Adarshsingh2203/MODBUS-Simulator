## MODBUS Client Tool

A lightweight, Python based MODBUS TCP client-server simulator built for testing the MODBUS protocol. Runs fully from the CLI on Windows.

Currently only supports CS and HRs with hardcoded values on the server end. 

### How to use it?

#### Simulating a Master:
On a command line, cd to MODBUS-Simulator/Client. Use the following command:

python modbus_client.py --ip [ip] --port [server_port] --fc [put FC=1 or 3] --address [starting_address] --count [number_of_points]

Sample command: 
python modbus_client.py --ip 127.0.0.1 --port 502 --fc 3 --address 0 --count 5

#### Simulating a Slave:
On a command line, cd to MODBUS-Simulator/Slave. Use the following command:

python modbus_server.py --port [server_port]

Sample command:
python modbus_server.py --port 502
