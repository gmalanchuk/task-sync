from rest_framework.exceptions import APIException


class CustomAPIException(APIException):
    def __init__(self, detail: str, status_code: int) -> None:
        self.detail = detail
        self.status_code = status_code
