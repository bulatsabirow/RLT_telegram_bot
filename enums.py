from enum import StrEnum


class GroupTypes(StrEnum):
    hour = "hour"
    day = "day"
    month = "month"


group_types_mapping = {
    GroupTypes.hour: "%Y-%m-%dT%H",
    GroupTypes.day: "%Y-%m-%d",
    GroupTypes.month: "%Y-%m",
}
