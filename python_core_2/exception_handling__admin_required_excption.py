from typing import Callable


class PermissionDeniedError(Exception):
    def __str__(self) -> str:
        return "User must be admin!"


class UnauthenticatedError(Exception):
    def __str__(self) -> str:
        return "Authentication credentials were not provided!"


def login_required(func: Callable) -> Callable:
    def wrapper(request: dict) -> None:
        if request.get("user") is None:
            raise UnauthenticatedError
        return func(request)

    return wrapper


def admin_required(func: Callable) -> Callable:
    def wrapper(request: dict) -> None:
        if request["user"]["is_admin"] is False:
            raise PermissionDeniedError
        return func(request)

    return wrapper


@login_required
@admin_required
def access_admin_page(request: dict) -> None:
    print(f"Welcome to the admin page, {request['user']['full_name']}")
