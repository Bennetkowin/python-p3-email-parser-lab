import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):
        # Use regex to split by commas or spaces
        emails = re.split(r'[,\s]+', self.email_addresses)
        
        # Remove empty strings, get unique emails, and sort alphabetically
        return sorted(set(filter(None, emails)))

