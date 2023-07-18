import time
import sys
from datetime import datetime
from pythonping import ping

from availability_data import load_availability_data, save_availability_data
from device_data import load_device_data
from commands import list_devices, add_device, delete_device, edit_device

ping_interval = 300  # 5 minutes

def ping_devices(device_data):
    """
    Ping devices and update the availability data.

    Args:
        device_data (list): List of dictionaries containing device data.
    """       
    availability_data = load_availability_data()
    current_time = datetime.now().strftime('%d-%m-%Y %H:%M')

    for device in device_data:
        device_id = device['device_id']
        device_name = device['device_name']
        ip = device['ip']
        try:
            response = ping(ip, count=1, timeout=2)
            status = 1 if response.success() else 0
        except:
            status = 0

        availability_data.append({
            'device_id': device_id,
            'status': status,
            'device_name':device_name,
            'timestamp': current_time
        })

    save_availability_data(availability_data)
    

def main():
    """
    Main function to run the availability monitoring process and other commands(commands like list-device, add-device, delete-device, update-device).
    """      
    device_data = load_device_data()

    if len(sys.argv) > 1:
        if sys.argv[1] == 'list-devices':
            list_devices(device_data)
        elif sys.argv[1] == 'add-device':
            add_device(device_data)
        elif sys.argv[1] == 'delete-device':
            if len(sys.argv) > 2:
                delete_device(device_data, sys.argv[2])
            else:
                print("You need to enter this command followed by a device id")
        elif sys.argv[1] == 'edit-device':
            if len(sys.argv) > 2:
                edit_device(device_data, sys.argv[2])
            else:
                print("You need to enter this command followed by a device id")
        else:
            print("Invalid Command")
    else:
        while True:
            ping_devices(device_data)
            time.sleep(ping_interval)
if __name__ == '__main__':
    main()
