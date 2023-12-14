import re
from typing import Any

from django.shortcuts import get_object_or_404
from rest_framework import status

from config.settings import logger
from tasks.exceptions import CustomAPIException
from tasks.grpc_services.permission import check_role_and_userid
from tasks.models import Board


class Checks:
    @staticmethod
    def __check_role_and_userid(request: Any) -> dict | None:
        token = request.COOKIES.get("access_token")
        return check_role_and_userid(token)

    def is_authenticated(self, request: Any, *args: Any, **kwargs: Any) -> dict | None:
        role_and_userid = self.__check_role_and_userid(request)
        return role_and_userid

    def is_staff(self, request: Any, *args: Any, **kwargs: Any) -> dict | None:
        role_and_userid = self.is_authenticated(request)

        if role_and_userid and role_and_userid["role"] not in ("staff", "admin"):
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return role_and_userid

    def is_admin(self, request: Any, *args: Any, **kwargs: Any) -> dict | None:
        role_and_userid = self.is_staff(request)

        if role_and_userid and role_and_userid["role"] != "admin":
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return role_and_userid

    def is_admin_or_owner(self, request: Any, *args: Any, **kwargs: Any) -> None:
        """ONLY FOR 'PUT', 'PATCH', 'DELETE' METHODS"""

        role_and_userid = self.__check_role_and_userid(request)
        if role_and_userid:
            user_id = role_and_userid["user_id"]

            if user_id and request.method in ("PUT", "PATCH", "DELETE"):
                match = re.search(r"\d+", request.path_info)
                if match:
                    board_id = match.group(0)
                    board_owner_id = get_object_or_404(Board, id=board_id).owner_id

                    if board_owner_id != user_id:
                        self.is_admin(request)
            else:
                logger.error("The is_admin_or_owner decorator can only be used in the PUT, PATCH, DELETE methods")
