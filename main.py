from storage import Storage
from pathlib import Path
lazy import user
lazy import time
from status import Status
import ui
from studytracker import StudyTracker
import validate

fp = Path(__file__).parent / 'data' / 'study.json'
data = Storage(fp)
print(f'{'='*50}\n{'Welcome to LabLog'.center(50)}\n{'='*50}')
if data.exists(): json_data = data.load()
else:
    print('Are you a new user?\n0. No\n1. Yes')
    while True:
        try:
            choice = int(input('Reply: '))
            if choice not in (0, 1):
                raise ValueError('Choose either 0 for No or 1 for Yes.')
            else: break
        except ValueError as e:
            print(e)
            time.sleep(1.5)
            ui.clear_last_lines(2)
    if choice==1:
        json_data = user.create_new_user()
        data.save(json_data)
        print(f'User {json_data['name']} created')
        input("Press enter to continue...")

    elif choice==1:
        print('The user file is missing so either place the user file at {fp} or create a new account')
        time.sleep(0.5)
        print('Thank you using LabLog. Exiting....')
        time.sleep(2)
        quit()

manager = StudyTracker(json_data)

options = [
    'Add a topic',
    'Delete a topic',
    'List all topics',
    'Search a topic',
    'Filter topics by status',
    'Change status of a topic'
]
while True:
    ui.clear_screen()
    print(f'{'='*50}\n{f'Welcome to LabLog, {json_data['name']}'.center(50)}\n{'='*50}')
    for i, option in enumerate(options, start=1):
        print(f'{i}. {option}')
    print('0. exit')

    while True:
        try:
            reply = int(input('Choose an option: '))
            if reply not in range(7):
                raise ValueError
            break
        except ValueError:
            print('Please! Choose a valid option.')
            time.sleep(1.5)
            ui.clear_last_lines(2)

    if reply is 1:
        ui.clear_screen()
        print(f'{'='*50}\n{f'{options[reply-1]}'.center(50)}\n{'='*50}')
        topic_name = validate.valid_topic_name()
        status_list = Status.all_values()
        for i, st in enumerate(status_list, start=1):
            print(f'{i}. {st}')
        s = validate.valid_status(status_list)
        note = input("Enter a note or press enter to skip.")
        t = 1 if input("Would like to add tags or enter to skip").strip() else 0
        if t:
            tags = []
            while True:
                tag = input("Enter a tag or press enter to proceed").strip()
                if tag: tags.append(tag)
                else: break
        job = manager.add_topic(topic_name, s, note, tags)
        if job:
            json_data['topics'] = manager.topics
            data.save(json_data)
            print(f'Added topic {topic_name}')
        else:
            print(f'Failed! Topic {topic_name} already exist')
            input('press enter to continue...')