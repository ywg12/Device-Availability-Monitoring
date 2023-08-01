from .device_monitor import DeviceMonitor

def main():
    """
    Entry point for running the device availability monitoring and management script.
    
    """
    device_monitor = DeviceMonitor("availability_data.csv", "device_data.json")
    device_monitor.main()    
if __name__ == '__main__':
    main()
