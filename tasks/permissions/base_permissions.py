import re
from typing import Any

from django.db.models import Model
from django.shortcuts import get_object_or_404
from rest_framework import status

from config.settings import logger
from tasks.exceptions import CustomAPIException
from tasks.grpc_services.permission import check_role_and_userid


class BasePermissions:
    @staticmethod
    def __check_role_and_userid(request: Any) -> dict:
        token = request.COOKIES.get("access_token")
        return check_role_and_userid(token)

    def is_authenticated(self, request: Any, *args: Any, **kwargs: Any) -> dict:
        role_and_userid = self.__check_role_and_userid(request)
        return role_and_userid

    def is_staff(self, request: Any, *args: Any, **kwargs: Any) -> dict:
        role_and_userid = self.is_authenticated(request)

        if role_and_userid["role"] not in ("staff", "admin"):
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return role_and_userid

    def is_admin(self, request: Any, *args: Any, **kwargs: Any) -> dict:
        role_and_userid = self.is_staff(request)

        if role_and_userid["role"] != "admin":
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return role_and_userid

    def is_admin_or_owner(self, request: Any, model: Model, *args: Any, **kwargs: Any) -> None:
        """ONLY FOR 'PUT', 'PATCH', 'DELETE' METHODS"""

        role_and_userid = self.__check_role_and_userid(request)
        if role_and_userid:
            current_user_id = role_and_userid["user_id"]

            if request.method in ("PUT", "PATCH", "DELETE"):
                match = re.search(r"\d+", request.path_info)
                if match:
                    obj_id = match.group(0)
                    obj_owner_id = get_object_or_404(model, id=obj_id).owner_id
                    if obj_owner_id != current_user_id:
                        self.is_admin(request)
            else:
                logger.error("The is_admin_or_owner decorator can only be used in the PUT, PATCH, DELETE methods")
