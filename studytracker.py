from topic import Topic
from status import Status
from datetime import date

class StudyTracker:
    topics: dict

    def __init__(self, json_data: dict) -> None:
        self.topics = {t: Topic(status=Status(json_data['topics'][t]['status']), created=json_data['topics'][t]['created'], modified=json_data['topics'][t]['modified'], note=json_data['topics'][t]['note'], tags=json_data['topics'][t]['tags']) for t in json_data['topics']}

    def to_dict(self, json_data: dict) -> dict:
        json_data['topics'] = {t: {
            'status': self.topics[t].status.value,
            'created': self.topics[t].created,
            'modified': self.topics[t].modified,
            'tags': self.topics[t].tags,
            'note': self.topics[t].note} for t in self.topics}
        return json_data

    def add_topic(self, topic_name: str, s: Status, note='', tags: list[str] =[]) -> bool:
        if topic_name not in self.topics:
            self.topics[topic_name] = Topic(s, note=note, tags=tags)
            return True
        return False

    def delete_topic(self, topic_name: str) -> bool:
        if topic_name in self.topics:
            del self.topics[topic_name]
            return True
        return False

    def search_topic(self, topic_name: str) -> list:
        result = []
        for i in self.topics:
            if topic_name in i:
                result.append(i)
        return result

    def filter_by_status(self, s: Status) -> list:
        result = []
        for topic in self.topics:
            if s is self.topics[topic].status:
                result.append(topic)
        return result


    def change_status(self, topic_name: str, s: Status) -> bool:
        if topic_name in self.topics:
            self.topics[topic_name].status = s
            self.topics[topic_name].modified = str(date.today())
            return True
        return False