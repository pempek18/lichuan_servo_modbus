from pymodbus.client import ModbusSerialClient as ModbusClient

def write_single_register(client, address, value):
    response = client.write_register(address, value, slave=1)
    return response

def write_multiple_registers(client, start_address, values):
    response = client.write_registers(start_address, values, slave=1)
    return response

def read_register(client, address):
    response = client.read_holding_registers(address, count=1, slave=1)
    return response

def read_multiple_registers(client, start_address, count):
    response = client.read_holding_registers(start_address, count=count, slave=1)
    return response