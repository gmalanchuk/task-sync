from typing import Any

from tasks.exceptions import CustomAPIException
from tasks.grpc_services.permission import check_permission


class Checks:
    @staticmethod
    def __permission_check(request: Any):
        token = request.COOKIES.get("access_token")
        return check_permission(token)

    def is_authenticated(self, request: Any, *args: Any, **kwargs: Any):
        role_or_error_message = self.__permission_check(request)
        if isinstance(role_or_error_message, dict):
            raise CustomAPIException(detail=role_or_error_message["data"], status_code=role_or_error_message["status"])
        return True

    # def is_staff(self):
    #
    # def is_admin(self):
