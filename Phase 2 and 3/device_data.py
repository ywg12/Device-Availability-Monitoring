import json

device_data_file = "device_data.json"

def load_device_data():
    """
    Load device data from the JSON file.

    Returns:
        list: List of dictionaries containing device data.
    """       
    with open(device_data_file) as file:
        device_data = json.load(file)
    return device_data
