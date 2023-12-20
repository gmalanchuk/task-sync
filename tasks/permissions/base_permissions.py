import re
from typing import Any

from django.db.models import Model
from django.shortcuts import get_object_or_404
from rest_framework import status

from config.settings import logger
from tasks.exceptions import CustomAPIException
from tasks.grpc_services.user import get_user_info


class BasePermissions:
    @staticmethod
    def __get_user_info(request: Any) -> dict:
        token = request.COOKIES.get("access_token")
        return get_user_info(token)

    def is_authenticated(self, request: Any, *args: Any, **kwargs: Any) -> dict:
        user_info = self.__get_user_info(request)
        return user_info

    def is_staff(self, request: Any, *args: Any, **kwargs: Any) -> dict:
        user_info = self.is_authenticated(request)

        if user_info["role"] not in ("staff", "admin"):
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return user_info

    def is_admin(self, request: Any, *args: Any, **kwargs: Any) -> dict:
        user_info = self.is_staff(request)

        if user_info["role"] != "admin":
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return user_info

    def is_admin_or_owner(self, request: Any, model: Model, *args: Any, **kwargs: Any) -> None:
        """ONLY FOR 'PUT', 'PATCH', 'DELETE' METHODS"""

        user_info = self.__get_user_info(request)
        if user_info:
            current_user_id = user_info["user_id"]

            if request.method in ("PUT", "PATCH", "DELETE"):
                match = re.search(r"\d+", request.path_info)
                if match:
                    obj_id = match.group(0)
                    obj_owner_id = get_object_or_404(model, id=obj_id).owner_id
                    if obj_owner_id != current_user_id:
                        self.is_admin(request)
            else:
                logger.error("The is_admin_or_owner decorator can only be used in the PUT, PATCH, DELETE methods")
