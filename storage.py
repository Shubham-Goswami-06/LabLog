import json, os

class Storage:
    filepath: str

    def __init__(self, filepath) -> None:
        self.filepath = filepath

    def exists(self) -> bool:
        return os.path.exists(self.filepath)

    def load(self) -> dict:
        with open(self.filepath, 'r') as f:
            return json.load(f)

    def save(self, data: dict) -> None:
        with open(self.filepath, 'w') as f:
            json.dump(data, f)