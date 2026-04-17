# all other custom exception should inherit from 'AppError' class
from app.core.response_code import response_codes


class AppError(Exception):
    def __init__(self, message, status_code, code:response_codes, data=None):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.code = code.value
        self.data = data    


class UserNotFound(AppError):
    # above all init get as it is from AppError
    pass

class UserAlreadyExists(AppError):
    # this is for add extra field
    def __int__(self, message, status_code, code:response_codes, explanation):
        super().__init__(message, status_code, code)
        self.explanation = explanation

class UserLogedIn(AppError):
    # this is only accept message and status_code
    def __init__(self, message, status_code):
        super().__init__(message, status_code)