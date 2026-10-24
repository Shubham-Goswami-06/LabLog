import data

def add(topic_name: str, s: str, log: dict):
    if topic_name in log['topics']:
        return f'Operation failed! Topic {topic_name} already exist.'
    else:
        log['topics'][topic_name] = s
        data.save(log)
        return f'Topic {topic_name} added successfully.'

def delete(topic_name, log: dict):
    if topic_name in log['topics']:
        del log['topics'][topic_name]
        data.save(log)
        return f'Topic {topic_name} deleted.'
    else:
        return f'Topic {topic_name} doesn\'t exist.'


def search(topic_name, log: dict):
    for topic, status in log['topics'].items():
        if(topic == topic_name):
            return f'{topic}: {status}'
    else:
        return f'Topic "{topic_name}" not found.'


def change_status(topic_name: str, new_status: str, log: dict):
    if topic_name in log['topics']:
        log['topics'][topic_name] = new_status
        data.save(log)
        return f'Topic {topic_name} status changed to {new_status}'
    else: return f'Topic {topic_name} not fount.'

def filter_by_status(status: str, log: dict):
    filtered_topics = [topic for topic, stat in log['topics'].items() if stat == status]
    return filtered_topics
