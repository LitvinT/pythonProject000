from aiogram import Router

from .main_panel import user_main_panel


user_router = Router(name='user_router')
user_router.include_router(router=user_main_panel)



__all__: list[str] = [
    'user_router'
]
