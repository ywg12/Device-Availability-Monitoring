import csv

class AvailabilityData:
    """
    AvailabilityData class provides functionality to load and save device availability data from/to a CSV file.

    Attributes:
        file_path (str): The file path to the CSV file containing availability data.
    """    
    def __init__(self, file_path):
        """
        Initializes AvailabilityData with the path to the CSV file containing availability data.
        """        
        self.file_path = file_path

    def load_availability_data(self):
        """
        Load availability data from the CSV file.

        Returns:
            list: A list of dictionaries containing availability data loaded from the CSV file.
        """        
        try:
            with open(self.file_path, 'r') as file:
                reader = csv.DictReader(file)
                availability_data = list(reader)
            return availability_data
        except FileNotFoundError:
            return []

    def save_availability_data(self, availability_data):
        """
        Save availability data to the CSV file.
        """        
        fieldnames = ['device_id', 'device_name', 'status', 'timestamp']
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(availability_data)
