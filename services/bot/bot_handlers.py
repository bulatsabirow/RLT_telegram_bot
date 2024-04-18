from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

from db import collection
from db.mongo import MongoDBService
from logger import logger
from services.handlers import TelegramDataHandler

mongo_service = MongoDBService(collection)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"Received start command from {update.effective_user}")
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.mention_markdown_v2()}!", parse_mode=ParseMode.MARKDOWN
    )


async def send_salary_aggregation_data(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    logger.info(
        f"Received message about salary aggregation data: {update.message.text}\n"
        f" from {update.effective_user}"
    )
    try:
        data_handler = TelegramDataHandler(update.message.text, mongo_service)
    except ValueError as exc:
        response = exc.args[0]
    else:
        response = str(await data_handler.serialize_response())
    await update.message.reply_text(response)
