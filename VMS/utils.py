from rest_framework.response import Response
from rest_framework import status

DEFAULT_SUCCESS_MSG='Successful'

def response_generator(status_code, data=None, error_msg=None, success_msg=DEFAULT_SUCCESS_MSG, debug_message=None, status=200):
    if status_code:
        response_data = {"message": success_msg, "data": data or {}, "status_code": status}
    else:
        error = {"message": error_msg, "status_code": status}
        if debug_message:
            error["debug_message"] = debug_message
        if data:
            error["data"] = data
              
        return {"status": 0, "error": error}

    return {"status": 1, "response_data": response_data}