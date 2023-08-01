import json

class DeviceData:
    """
    DeviceData class provides functionality to load device data from a JSON file.

    Attributes:
        file_path (str): The file path to the JSON file containing device data.
    """    
    def __init__(self, file_path):
        self.file_path = file_path

    def load_device_data(self):
        with open(self.file_path) as file:
            device_data = json.load(file)
        return device_data
