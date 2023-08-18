import ipaddress

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
