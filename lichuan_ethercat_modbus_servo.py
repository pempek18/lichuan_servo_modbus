from modbus import modbus_functions
import re

def validate_and_convert(input_string):
    # Define the regex pattern for the format P02-17
    pattern = r'^(0x)?([0-9A-Fa-f]+)-(0x)?([0-9A-Fa-f]+)$'
    
    # Match the input string against the pattern
    match = re.fullmatch(pattern, input_string)
    combined_string = ""
    combined_number = 0
    format_fit = False
    if match:
        format_fit = True
        # Extract the numeric parts
        part1 = match.group(2)
        part2 = match.group(4)
        combined_string = f"P{part1}-{part2}"
        part2_int = int(part2)
        if part2_int <= 15 :
            part2 = "0" + hex(int(part2))[2:]
        else :
            part2 = hex(int(part2))[2:]
        string_for_hex = part1 + str(part2)
        print(f"string to hex: {string_for_hex}")

        combined_number = int(string_for_hex, 16)
        print(f"addres: {combined_number}")
        return format_fit, combined_number, combined_string
    else:
        print(ValueError("Input string does not match the required format 'XX-XX'"))
        return False

def check_any_parameter_from_console():
    # Configure the serial client
    client = modbus_functions.ModbusClient(method='rtu', port='COM11', baudrate=19200, stopbits=1, bytesize=8, parity='E')
    if not client.connect():
        print("Failed to connect to the device.")
        return
    try:
        while True :
            # 1. Read value from register given register
            address = input("Give hex falue in format 00-11 where 00 is P and 11 is number like P02-17 is 02-17:  ") #0x0211
            valid, parameter_int, parameter_string = validate_and_convert(address)
            if valid :
                response = modbus_functions.read_register(client, parameter_int)
                if response.isError():
                    print(f"Failed to read register {parameter_string}.")
                    break
                else:
                    print(f"Value read from {parameter_string} : {response.registers[0]}")
            else:
                print("wrong format")
    finally:
        client.close()   
if __name__ == "__main__" :
    check_any_parameter_from_console() 