from pymodbus.client import ModbusTcpClient
import argparse

def read_registers(ip, port, unit, address, count, fc):

    # setup the client context
    client = ModbusTcpClient(ip, port=port)
    client.connect()

    # for now, we only support FC = 0x01 and 0x03
    # so, we can just read the CS or HR values
    if fc == 0x03:
        response = client.read_holding_registers(address=address, count=count, unit=unit)
    elif fc == 0x01:
        response = client.read_coils(address=address, count=count, unit=unit)
    # implement an else condition for safety
    else:
        print(f"Haven't really implemented any support for : {fc}")
        client.close()
        return

    if response.isError():
        print("Error reading data:", response)
    else:
        print("Response:")
        if fc == 3:
            print(f"Holding Registers [{address}–{address+count-1}]: {response.registers}")
        elif fc == 1:
            print(f"Coils [{address}–{address+count-1}]: {response.bits}")

    # once done, shut down the client
    client.close()

if __name__ == "__main__":
    # parse the input parameters
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help="Server IP")
    parser.add_argument("--port", type=int, default=5020, help="Server Port")
    parser.add_argument("--unit", type=int, default=1, help="Unit ID")
    parser.add_argument("--address", type=int, default=0, help="Starting address")
    parser.add_argument("--count", type=int, default=5, help="Number of items to read")
    parser.add_argument("--fc", type=int, default=3, choices=[1, 3], help="Function code: 1=Read Coils, 3=Read Holding Registers")
    args = parser.parse_args()

    # read the specified type and no. of points
    read_registers(args.ip, args.port, args.unit, args.address, args.count, args.fc)
