from rest_framework.exceptions import APIException


class ProfileDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested profile does not exist.'


class UserIsNotAuthenticated(APIException):
    status_code = 403
    default_detail = 'You should be logged in to proceed.'


class RouterException(Exception):
    message = ""
    

    def __init__(self, msg) -> None:
        self.message = msg
class BinpackingException(Exception):
    message = ""
    

    def __init__(self, msg) -> None:
        self.message = msg


class ExportingException(Exception):
    """
    Raised when a exporting  encounters an error
    """
    
    message = ""
    

    def __init__(self, msg) -> None:
        self.message = msg
        
class SmsException(Exception):
    """Exception raised SMS encounters an error """
    message = ""

    def __init__(self, msg) -> None:
        self.message = msg