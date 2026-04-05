from clerk_backend_api import Clerk
# from clerk_backend_api.models import SDKError
from fastapi.responses import JSONResponse

class AuthonticationService:

    def __init__(self, bearer_token):
        try:
            self.auth = Clerk(bearer_auth=bearer_token)
            print('handshake with clerk successfull')
        except Exception as e:
            return JSONResponse(status_code=e.status_code, content={'message' : e.message})

    def get_auth(self):
        return self.auth