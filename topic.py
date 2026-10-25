from status import Status
from dataclasses import dataclass, field
from datetime import date

@dataclass
class Topic:
    status: Status
    created: date | None = None
    modified: date | None = None
    tags: list = field(default_factory = list)
    note: str = ""

    def __post_init__(self):
        if self.created is None:
            self.created = date.today()
        if self.modified is None:
            self.modified = self.created
        else:
            self.modified = date.today()