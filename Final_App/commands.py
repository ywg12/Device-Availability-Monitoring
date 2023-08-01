import json
from pythonping import ping
from tabulate import tabulate
from .utility import IPUtility

class CommandHandler:
    def list_devices(self, device_data):
        """
        List Devices from the device_data list in a readable format on the screen.
        """        
        table_data = []
        for device in device_data:
            table_data.append([device['device_id'], device['device_name'], device['ip']])

        headers = ['Device ID', 'Device Name', 'IP Address']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))

    def add_device(self, device_data):
        """
        Add a new device inputted by the user and saves it into the device_data list.
        """
        device_id = input("Enter device ID: ")
        for device in device_data:
            if device['device_id'] == device_id:
                print("Device ID already exists.")
                return
        device_name = input("Enter device name: ")
        ip_address = input("Enter IP address: ")
        if IPUtility.is_valid_ip(ip_address):
            device_data.append({
                'device_id': device_id,
                'device_name': device_name,
                'ip': ip_address
            })

            with open('device_data.json', 'w') as file:
                json.dump(device_data, file, sort_keys=True, indent=4)

            print("Device added successfully.")
        else:
            print("Invalid IP")

    def delete_device(self, device_data, device_id):
        """
        Deletes a device entry from the device_data list.
        """
        for device in device_data:
            if device['device_id'] == device_id:
                device_data.remove(device)
                with open('device_data.json', 'w') as file:
                    json.dump(device_data, file)
                print("Device deleted successfully.")
                return

        print("Device ID not found.")

    def edit_device(self, device_data, device_id):
        """
        Edits a device entry by the device ID inputted by the user. Only the device_name and ip_address can be changed.
        """
        for device in device_data:
            if device['device_id'] == device_id:
                device['device_name'] = input("Enter new device name: ")
                device['ip'] = input("Enter new IP address: ")
                if IPUtility.is_valid_ip(device['ip']):
                    with open('device_data.json', 'w') as file:
                        json.dump(device_data, file)
                    print("Device updated successfully.")
                    return
                else:
                    print("Invalid IP")
                    return

        print("Device ID not found.")
          
    def ping_device(self, ip):
        """
        Pings the given IP address and prints the device's online status.
        """
        try:
            response = ping(ip, count=1, timeout=2)
            status = 1 if response.success() else 0
        except:
            status = 0
        if status == 1:
            print("The device is online.")
        else: 
            print("The device is either offline or not reachable at the moment.")
        
