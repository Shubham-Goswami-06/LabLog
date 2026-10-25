from topic import Topic
from status import Status

class StudyTracker:
    topics: dict

    def __init__(self, json_data) -> None:
        self.topics = {t: Topic(status=Status(t['status']), created=t['created'], modified=t['modified'], note=t['note'], tags=t['tags']) for t in json_data['topics']}

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
            return True
        return False