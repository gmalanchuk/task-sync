from typing import Any

from rest_framework import status

from tasks.exceptions import CustomAPIException
from tasks.grpc_services.permission import check_role, check_userid


class Checks:
    @staticmethod
    def __сheck_role(request: Any) -> dict | str | None:
        token = request.COOKIES.get("access_token")
        return check_role(token)

    @staticmethod
    def __сheck_userid(request: Any) -> dict | str | None:
        token = request.COOKIES.get("access_token")
        return check_userid(token)

    def is_authenticated(self, request: Any, *args: Any, **kwargs: Any) -> CustomAPIException | str | None:
        role_or_error_message = self.__сheck_role(request)
        if isinstance(role_or_error_message, dict):
            raise CustomAPIException(detail=role_or_error_message["data"], status_code=role_or_error_message["status"])

        return role_or_error_message

    def is_staff(self, request: Any, *args: Any, **kwargs: Any) -> CustomAPIException | str:
        role = self.is_authenticated(request)

        if role not in ("staff", "admin"):
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return role

    def is_admin(self, request: Any, *args: Any, **kwargs: Any) -> CustomAPIException | str:
        role = self.is_staff(request)

        if role != "admin":
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return role

    def is_admin_or_owner(self, request: Any, *args: Any, **kwargs: Any) -> CustomAPIException | None:
        # todo  достать из куки токен
        # todo отправить его в сервис аутентификации и получить айдишник пользователя
        # todo сверить полученный айди с owner_id
        # todo

        role = self.is_admin(request)
        print(self.__сheck_userid(request))

        if role == "admin":
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return None
