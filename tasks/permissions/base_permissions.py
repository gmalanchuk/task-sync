import re

from django.db.models import Model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request

from config.settings import logger
from tasks.exceptions import CustomAPIException
from tasks.grpc_services import get_user_info_by_token


class BasePermissions:
    def is_authenticated(self, request: Request, *args: tuple, **kwargs: dict) -> dict:
        user_info = get_user_info_by_token(request)
        return user_info

    def is_staff(self, request: Request, *args: tuple, **kwargs: dict) -> dict:
        user_info = self.is_authenticated(request)

        if user_info["role"] not in ("staff", "admin"):
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return user_info

    def is_admin(self, request: Request, *args: tuple, **kwargs: dict) -> dict:
        user_info = self.is_staff(request)

        if user_info["role"] != "admin":
            raise CustomAPIException(
                detail="Permission Denied: You do not have sufficient privileges to perform this action",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return user_info

    def is_admin_or_owner(self, request: Request, model: Model, *args: tuple, **kwargs: dict) -> None:
        """ONLY FOR 'PUT', 'PATCH', 'DELETE' METHODS"""

        user_info = get_user_info_by_token(request)
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
