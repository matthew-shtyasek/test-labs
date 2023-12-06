from aiogram import Router
from lab1.routing.settings import router as settings_router
from lab1.routing.main_menu import router as menu_router

router = Router()
router.include_router(settings_router)
router.include_router(menu_router)
