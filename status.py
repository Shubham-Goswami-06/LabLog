from enum import Enum

class Status(Enum):
    complete = "Complete"
    currently_studying = 'Currently Studying'
    not_statrted = "Not Started"

    @classmethod
    def all_values(cls) -> list[str]:
        return [i.value for i in cls]