class InvalidRequestTypeException(BaseException):
    status_code : 400
    default_code : 'invalid_request_type'
    default_detail_code : 'invalid_request_type_error'

