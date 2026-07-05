# import boto3
from brevo import Brevo

class EmailService:

    def __init__(self, key):
        self.client = Brevo(api_key=key)

    def get_email(self):
        # return email client
        return self.client