import email
import os
from dotenv import load_dotenv
from .logs import LoggerService
from .db import DatabaseService
from logging import Logger
from supabase import Client
from .auth import AuthonticationService
from clerk_backend_api import Clerk
from .email import EmailService
# import boto3
from mypy_boto3_ses import SESClient
from .cache import CachService
from upstash_redis import Redis
from .queu import QueueService
from qstash.client import QStash
from brevo import Brevo

# this is for check where this instance run ( production or local )
# according to the above, bellow files are loaded
server = os.getenv('production', 'test')

if server == 'test':
    load_dotenv(dotenv_path='.env.test')
else:
    load_dotenv(dotenv_path='.env')

class service_initiate():

    def __init__(self):
        # all initiated servicess store in this dictionary
        self.services = {}

        # Initiate Logging
        log_service = LoggerService(os.getenv('source_token'), os.getenv('ingesting_host'))
        self.services['logger'] = log_service.get_logger()
        
        # Initiate Database
        db = DatabaseService(os.getenv('supabase_url'), os.getenv('supabase_key'))
        self.services['db'] = db.get_db()
        
        # Initiate Authontication
        auth = AuthonticationService(os.getenv('CLERK_SECRET_KEY'))
        self.services['auth'] = auth.get_auth()
        
        # Initiate Email-serviceresponse
        email = EmailService(os.getenv('email_key'))
        self.services['email'] = email.get_email()
        # email = EmailService(os.getenv('email_key'), os.getenv('aws_secret_access_key'), os.getenv('region'))
        # self.services['email'] = email.get_email()
        
        # Initiate the chaching system
        cache = CachService(os.getenv('UPSTASH_REDIS_REST_URL'), os.getenv('UPSTASH_REDIS_REST_TOKEN'))
        self.services['cache'] = cache.get_cache()

        queue = QueueService(os.getenv("QSTASH_TOKEN"))
        self.services['queue'] = queue.get_queue()

    def logger(self) -> Logger:
        # return the logger
        return self.services.get('logger')

    def db(self) -> Client:
        # get database connection
        return self.services.get('db')

    def auth(self) -> Clerk:
        # get authontication connection
        return self.services.get('auth')

    def email(self) -> Brevo:
        # get email sender client
        return self.services.get('email')

    def cache(self) -> Redis:
        # get redis cache client
        return self.services.get('cache')
    
    def queue(self) -> QStash:
        return self.services.get('queue')

service_container = service_initiate()