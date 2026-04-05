import boto3

class EmailService:

    def __init__(self, access_key_id, secrete_access_key, region):
        # initiate the AWS-Email service
        self.client = boto3.client('ses', aws_access_key_id=access_key_id, aws_secret_access_key=secrete_access_key, region_name=region)

    def get_email(self):
        # return email client
        return self.client