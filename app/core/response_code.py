from enum import Enum

class response_codes(str, Enum):
    user_created = 'USER_CREATED'
    user_not_created = 'USER_NOT_CREATED'
    user_not_found = 'USER_NOT_FOUND'
    user_deleted = 'USER_DELETED'
    email_sent = 'EMAIL_SENT'
    internal_server_error = 'INTERNAL_SERVER_ERROR'
