import datetime
from dataclasses import dataclass, field

from enums import GroupTypes


@dataclass
class TelegramMessage:
    dt_from: datetime.datetime
    dt_upto: datetime.datetime
    group_type: GroupTypes

    def __post_init__(self):
        self.dt_from = datetime.datetime.fromisoformat(self.dt_from)
        self.dt_upto = datetime.datetime.fromisoformat(self.dt_upto)
