import asyncio
import datetime
import json
from dataclasses import asdict
from pprint import pprint


from db import collection
from db.mongo import MongoDBService
from schema import TelegramMessage


class TelegramDataHandler:
    """
    Middleware that handles data to json format before sending them to Mongo Database Service
    and then to Telegram user.
    """

    def __init__(self, data: str, db_service: MongoDBService):
        self.data = data
        self._db_service = db_service

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        try:
            self._data = TelegramMessage(**json.loads(value))
        except (json.decoder.JSONDecodeError, TypeError):
            raise ValueError(
                'Невалидный запрос. Пример запроса: \
{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}'
            )

    @property
    def db_service(self):
        return self._db_service

    async def serialize_response(self):
        raw_data = await self.db_service.fetch_aggregated_data(**asdict(self.data))
        dataset = []
        labels = []

        for raw_doc in raw_data:
            dataset.append(raw_doc["total"])
            labels.append(datetime.datetime.isoformat(raw_doc["_id"]))

        return json.dumps({"dataset": dataset, "labels": labels})
