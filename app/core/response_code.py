from enum import Enum

class response_codes(Enum):
    user_created = 'USER_CREATED'
    user_not_found = 'USER_NOT_FOUND'
    user_deleted = 'USER_DELETED'
