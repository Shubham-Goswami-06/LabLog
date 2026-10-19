import json
from pathlib import Path

def load():
    file_path = Path(__file__).parent / 'data' / 'study.json'
    with open(file_path, 'r') as f:
        return json.load(f)

def save(d):
    file_path = Path(__file__).parent / 'data' / 'study.json'
    with open(file_path, 'w') as f:
        return json.dump(d, f, indent=4)