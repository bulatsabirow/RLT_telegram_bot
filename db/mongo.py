import datetime

from dateutil import relativedelta
from motor.motor_asyncio import AsyncIOMotorCollection

from enums import group_types_mapping, GroupTypes


class MongoDBService:
    def __init__(self, collection: AsyncIOMotorCollection):
        self._collection = collection

    @property
    def collection(self):
        return self._collection

    async def fetch_aggregated_data(
        self,
        dt_from: datetime.datetime,
        dt_upto: datetime.datetime,
        group_type: GroupTypes,
    ):
        # According to MongoDB documentation, upper bound is exclusive,
        # so this bound need to be incremented (+1 hour or +1 day or +1 month)
        lower_bound, upper_bound = dt_from, dt_upto + relativedelta.relativedelta(
            **{group_type: 1}
        )
        pipeline = [
            {
                "$densify": {
                    "field": "dt",
                    "range": {
                        "step": 1,
                        "unit": group_type,
                        "bounds": [lower_bound, upper_bound],
                    },
                }
            },
            {"$match": {"dt": {"$gte": dt_from, "$lte": dt_upto}}},
            {
                "$addFields": {
                    "temp": {
                        "$toDate": {
                            "$dateToString": {
                                "format": group_types_mapping[group_type],
                                "date": "$dt",
                            }
                        }
                    }
                }
            },
            {"$group": {"_id": "$temp", "total": {"$sum": "$value"}}},
            {"$sort": {"_id": 1}},
        ]
        return await self.collection.aggregate(
            aggregate="sample_collection", pipeline=pipeline
        ).to_list(None)
