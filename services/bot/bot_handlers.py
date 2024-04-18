from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from db import collection
from db.mongo import MongoDBService
from services.handlers import TelegramDataHandler

mongo_service = MongoDBService(collection)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.mention_markdown_v2()}!", parse_mode=ParseMode.MARKDOWN
    )


async def send_salary_aggregation_data(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    try:
        data_handler = TelegramDataHandler(update.message.text, mongo_service)
    except ValueError as exc:
        response = exc.args[0]
    else:
        response = str(await data_handler.serialize_response())

    await update.message.reply_text(response)
