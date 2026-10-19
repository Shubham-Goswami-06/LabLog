import data

def add(topic_name: str, s:int, status: list):
    log = data.load()
    log['topics'][topic_name] = status[s]
    data.save(log)

def delete(topic_name):
    log = data.load()
    del log['topics'][topic_name]
    data.save(log)


def search(topic_name):
    log = data.load()
    for topic, status in log['topics'].items():
        if(topic == topic_name):
            print(f'{topic}: {status}')
            break
    else:
        print(f'Topic "{topic_name}" not found.')

def show():
    # List all the topics
    log = data.load()
    for i, (topic, status) in enumerate(log['topics'].items(), start=1):
        print(f'{i}. {topic}: {status}', end='\n')

def change_status(topic_name: str, new_status: str):
    log = data.load()
    if topic_name in log['topics']:
        log['topics'][topic_name] = new_status
    data.save(log)

def filter_by_status(status: str):
    log = data.load()
    filtered_topics = {topic: stat for topic, stat in log['topics'].items() if stat == status}
    return filtered_topics
