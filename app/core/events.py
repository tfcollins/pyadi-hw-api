from typing import Callable

from fastapi import FastAPI


def create_start_app_handler(app: FastAPI) -> Callable:
    def start_app() -> None:
        """Nothing yet"""
        pass

    return start_app
