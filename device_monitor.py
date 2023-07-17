import json
import csv
import time
from datetime import datetime
from pythonping import ping

# JSON and CSV File Paths
availability_data_file = "availability_data.csv"
device_data_file = "device_data.json"

# Ping interval in seconds
ping_interval = 300  # 5 minutes

def load_device_data():
    """
    Load device data from the JSON file.

    Returns:
        list: List of dictionaries containing device data.
    """    
    with open(device_data_file) as file:
        device_data = json.load(file)
        #[{"device_id":"1", :} ]
    return device_data

def load_availability_data():
    """
    Load availability data from the CSV file.

    Returns:
        list: List of dictionaries containing availability data.
    """    
    try:
        with open(availability_data_file, 'r') as file:
            reader = csv.DictReader(file)
            availability_data = list(reader)
        return availability_data
    except FileNotFoundError:
        return []

def save_availability_data(availability_data):
    """
    Save availability data to the CSV file.

    Args:
        availability_data (list): List of dictionaries containing availability data.
    """    
    fieldnames = ['device_id', 'status', 'timestamp']
    with open(availability_data_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(availability_data)

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
        ip = device['ip']
        try:
            response = ping(ip, count=1, timeout=2)
            status = 1 if response.success() else 0
        except:
            status = 0

        availability_data.append({
            'device_id': device_id,
            'status': status,
            'timestamp': current_time
        })

    save_availability_data(availability_data)

def main():
    """
    Main function to run the availability monitoring process.
    """    
    device_data = load_device_data()
    while True:
        ping_devices(device_data)
        time.sleep(ping_interval)

if __name__ == '__main__':
    main()
