import asyncio
from pymodbus.server.async_io import StartAsyncTcpServer
from pymodbus.datastore import (
    ModbusServerContext,
    ModbusSlaveContext,
    ModbusSequentialDataBlock,
)
from pymodbus.device import ModbusDeviceIdentification
import argparse

async def run_server(ip: str, port: int, input_coils, holding_registers):

    # Create a datamap of the points we just made.
    # This means, we're storing the actual points in a pointlist
    # since we don't really use SQL or any other DB
    # here, we can simply create a local storage.
    store = ModbusSlaveContext(
        cs=ModbusSequentialDataBlock(0, input_coils),
        hr=ModbusSequentialDataBlock(0, holding_registers),
    )

    # set up the MODBUS Application layer Context
    Adarsh_MODBUS_Context = ModbusServerContext(slaves=store, single=True)

    # Define some additional meta-data
    identity = ModbusDeviceIdentification()
    identity.VendorName = "Adarsh"
    identity.ProductName = "Adarsh's MODBUS TCP Simulator"
    identity.ModelName = "AdarshPythonServer"
    identity.MajorMinorRevision = "1.0"

    print(f"MODBUS TCP Server running on {ip}:{port}")

    # actually start the server
    await StartAsyncTcpServer(
        context=Adarsh_MODBUS_Context,
        identity=identity,
        address=(ip, port),
    )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5020)
    args = parser.parse_args()

    # We are setting some default values for points here
    # For now, let's assume we have the following:
    # 10 Coil Status : All False
    # 10 Holding Registers : {100,200,300,400,500,600,700,800,900,1000} 
    input_coils = [False] * 10
    holding_registers = [100 * i for i in range(1, 11)]  

    # let's goooooo
    asyncio.run(run_server(args.ip, args.port, input_coils, holding_registers))
