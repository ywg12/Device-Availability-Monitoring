import time
import sys
from datetime import datetime
from pythonping import ping

from .availability_data import AvailabilityData
from .device_data import DeviceData
from .commands import CommandHandler
from .utility import ErrorLogger

ping_interval = 300  # 5 minutes

class DeviceMonitor:
    """
    DeviceMonitor class monitors the availability of devices and provides command line functionality to manage devices.

    Attributes:
        availability_data (AvailabilityData): An instance of AvailabilityData to manage availability data storage.
        device_data (DeviceData): An instance of DeviceData to manage device data storage.
        command_handler (CommandHandler): An instance of CommandHandler to handle command line operations.

    Methods:
        ping_devices(): Ping all the devices in the device_data list and update the availability data accordingly.
        main(): Main function to run the device availability monitoring and command line functionality.
    """
    def __init__(self, availability_file, device_file):
        """
        Initialize DeviceMonitor with availability and device data file paths.

        Parameters:
            availability_file (str): The file path for the availability data storage.
            device_file (str): The file path for the device data storage.
        """        
        self.availability_data = AvailabilityData(availability_file)
        self.device_data = DeviceData(device_file)
        self.command_handler = CommandHandler() 
        self.ErrorLogger = ErrorLogger()    

    def ping_devices(self):
        """
        Ping all the devices in the device_data list and update the availability data accordingly.
        """
        availability_data = self.availability_data.load_availability_data()
        current_time = datetime.now().strftime('%d-%m-%Y %H:%M')

        for device in self.device_data.load_device_data():
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
                'device_name': device_name,
                'timestamp': current_time
            })

        self.availability_data.save_availability_data(availability_data)

    def main(self):
        """
        Main function to run the device availability monitoring.
        """
        if len(sys.argv) > 1:
            if sys.argv[1] == 'list-devices':
                self.command_handler.list_devices(self.device_data.load_device_data())
            elif sys.argv[1] == 'add-device':
                self.command_handler.add_device(self.device_data.load_device_data())
            elif sys.argv[1] == 'delete-device':
                if len(sys.argv) > 2:
                    self.command_handler.delete_device(self.device_data.load_device_data(), sys.argv[2])
                else:
                    print("You need to enter this command followed by a device id")
            elif sys.argv[1] == 'edit-device':
                if len(sys.argv) > 2:
                    self.command_handler.edit_device(self.device_data.load_device_data(), sys.argv[2])
                else:
                    print("You need to enter this command followed by a device id")
            elif sys.argv[1] == 'ping':
                if len(sys.argv) > 2:
                    self.command_handler.ping_device(sys.argv[2])
                else:
                    print("You need to enter this command followed by an IP address")
            else:
                print("Invalid Command")
                print("----------------------------------------------------------------------------------")
                print("The following commands are executable.")
                print("list-devices -> To list the existing devices.")
                print("add-device -> To add a new device.")
                print("delete-device <device_id> -> To delete a device.")
                print("edit-device <device_id> -> To edit a device config.")
                ErrorLogger.log_custom_error("User entered an invalid command or incomplete command.")
                
        else:
            try:
                while True:
                    self.ping_devices()
                    time.sleep(ping_interval)
            except KeyboardInterrupt as e:
                self.ErrorLogger.log_error(f"An error occurred: {str(e)}")
                print("The operation was interrupted by user through keystroke")

if __name__ == '__main__':
    device_monitor = DeviceMonitor("availability_data.csv", "device_data.json")
    device_monitor.main()
