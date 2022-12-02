if __name__ == '__main__':
    from handlers import router
    from loader import dp, bot
    dp.include_router(router=router)
    dp.run_polling(bot)
