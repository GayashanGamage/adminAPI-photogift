import os
from supabase import create_client, Client

class DatabaseService():

    def __init__(self, url, key):
        # initiate database
        self.supabase: Client = create_client(url, key)
        
    def get_db(self):
        # return database
        return self.supabase
