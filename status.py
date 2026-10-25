from enum import Enum

class Status(Enum):
    complete = "Complete"
    not_statrted = "Not Started"
    incomplete = "Incomplete"

    @classmethod
    def all_values(cls) -> list[str]:
        return [i.value for i in cls]