import json

def list_devices(device_data):
    """List Devices from the Json format in a readable format on the screen.

    Args:
         device_data (list): List of dictionaries containing device data.
    """    
    for device in device_data:
        print(f"Device ID: {device['device_id']}")
        print(f"Device Name: {device['device_name']}")
        print(f"IP Address: {device['ip']}")
        print()
        
def add_device(device_data):
    """Add a new device inputted bythe user and saves it into the device_data.json.

    Args:
         device_data (list): List of dictionaries containing device data.
    """       
    device_id = input("Enter device ID: ")
    for device in device_data:
        if device['device_id'] == device_id:
            print("Device ID already exists.")
            return    
    device_name = input("Enter device name: ")
    ip_address = input("Enter IP address: ")

    device_data.append({
        'device_id': device_id,
        'device_name': device_name,
        'ip': ip_address
    })

    with open('device_data.json', 'w') as file:
        json.dump(device_data, file, sort_keys=True, indent=4)

    print("Device added successfully.")    

def delete_device(device_data, device_id):
    """Deletes a device entry from the device_data.json file.

    Args:
         device_data (list): List of dictionaries containing device data.
        device_id (str): Device_id whose entry has to be deleted.
    """    
    print('The type of device_is is ', type(device_id))
    for device in device_data:
        if device['device_id'] == device_id:
            device_data.remove(device)
            with open('device_data.json', 'w') as file:
                json.dump(device_data, file)
            print("Device deleted successfully.")
            return

    print("Device ID not found.")
    
def edit_device(device_data, device_id):
    """Edits a device_entry by the id inputted by the user. Only the device_name and ip_address can be changed.

    Args:
         device_data (list): List of dictionaries containing device data.
        device_id (str): Device_id whose entry has to be edited.
    """    
    for device in device_data:
        if device['device_id'] == device_id:
            device['device_name'] = input("Enter new device name: ")
            device['ip'] = input("Enter new IP address: ")
            with open('device_data.json', 'w') as file:
                json.dump(device_data, file)
            print("Device updated successfully.")
            return

    print("Device ID not found.")  