import ipaddress
import logging

class IPUtility:
    @staticmethod
    def is_valid_ip(ip_address):
        """
        Check if the given IP address is valid.
        """
        try:
            # Check if the IP address is a valid IPv4 or IPv6 address
            ipaddress.ip_address(ip_address)
            return True
        except ValueError:
            return False
class ErrorLogger:
    def __init__(self, log_file='error_log.log'):
        logging.basicConfig(
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=log_file,
            filemode='a'
        )

    @staticmethod
    def log_error(error_message):
        logging.error(error_message, exc_info=True)
        
    def log_custom_error(custom_error_message):
        logging.error(f"Error: {custom_error_message}")        