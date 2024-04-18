from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from config import TOKEN
from services.bot.bot_handlers import send_salary_aggregation_data, start


def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, send_salary_aggregation_data)
    )

    application.run_polling(allowed_updates=Update.ALL_TYPES)
