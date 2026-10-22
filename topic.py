import data

def add(topic_name: str, s: str, log: dict):
    log['topics'][topic_name] = s
    data.save(log)

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

def show(log: dict):
    # List all the topics
    for i, (topic, status) in enumerate(log['topics'].items(), start=1):
        print(f'{i}. {topic}: {status}', end='\n')

def change_status(topic_name: str, new_status: str, log: dict):
    if topic_name in log['topics']:
        log['topics'][topic_name] = new_status
    data.save(log)

def filter_by_status(status: str, log: dict):
    filtered_topics = [topic for topic, stat in log['topics'].items() if stat == status]
    return filtered_topics
