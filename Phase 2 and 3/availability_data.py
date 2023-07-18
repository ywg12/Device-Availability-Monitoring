import csv

availability_data_file = "availability_data.csv"

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
    fieldnames = ['device_id', 'device_name', 'status', 'timestamp']
    with open(availability_data_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(availability_data)
