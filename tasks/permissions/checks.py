from typing import Any

from rest_framework import status

from tasks.exceptions import CustomAPIException
from tasks.grpc_services.permission import check_permission


class Checks:
    @staticmethod
    def __permission_check(request: Any) -> dict | str | None:
        token = request.COOKIES.get("access_token")
        return check_permission(token)

    def is_authenticated(self, request: Any, *args: Any, **kwargs: Any) -> CustomAPIException | bool:
        role_or_error_message = self.__permission_check(request)
        if isinstance(role_or_error_message, dict):
            raise CustomAPIException(detail=role_or_error_message["data"], status_code=role_or_error_message["status"])

        return True

    def is_staff(self, request: Any, *args: Any, **kwargs: Any) -> CustomAPIException | bool:
        role_or_error_message = self.__permission_check(request)
        if isinstance(role_or_error_message, dict):
            raise CustomAPIException(detail=role_or_error_message["data"], status_code=role_or_error_message["status"])

        if role_or_error_message not in ("staff", "admin"):
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        return True

    def is_admin(self, request: Any, *args: Any, **kwargs: Any) -> CustomAPIException | bool:
        # TODO все права строятся на предыдущих
        role_or_error_message = self.__permission_check(request)
        if isinstance(role_or_error_message, dict):
            raise CustomAPIException(detail=role_or_error_message["data"], status_code=role_or_error_message["status"])

        if role_or_error_message != "admin":
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        return True
