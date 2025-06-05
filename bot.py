if __name__ == '__main__':
    from aiogram import executor
    from bot import dp  # если у тебя диспетчер в другом файле — укажи путь
    executor.start_polling(dp, skip_updates=True)
