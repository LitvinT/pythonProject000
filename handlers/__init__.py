from aiogram import Router, F

from .users import user_router


router = Router(name='main')
router.include_router(router=user_router)


__all__: list[str] = [
    'router'
]
