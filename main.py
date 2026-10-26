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

    elif choice==0:
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
            if reply not in range(len(options)):
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
        if topic_name == '0': continue
        status_list = Status.all_values()
        for i, st in enumerate(status_list, start=1):
            print(f'{i}. {st}')
        s = validate.valid_status(status_list)
        note = input("Enter a note or press enter to skip: ")
        tags = []
        while True:
            tag = input("Enter a tag or press enter to proceed: ").strip()
            if tag: tags.append(tag)
            else: break
        job = manager.add_topic(topic_name, s, note, tags)
        if job:
            json_data = manager.to_dict(json_data)
            data.save(json_data)
            print(f'Added topic {topic_name}')
            input('press enter to continue...')
        else:
            print(f'Failed! Topic {topic_name} already exist')
            input('press enter to continue...')

    elif reply is 2:
        print(f'{'='*50}\n{f'{options[reply-1]}'.center(50)}\n{'='*50}')
        topic_name = validate.valid_topic_name()
        if topic_name == '0': continue
        while True:
            try:
                confirm = int(input('Are you sure ?\n0. No\n1. Yes\n--> '))
                if confirm not in (0,1):
                    raise ValueError
                else: break
            except ValueError:
                print('Please select a valid option.')
                time.sleep(1.5)
                ui.clear_last_lines(5)

        if confirm is 0: continue
        else:
            del manager.topics[topic_name]
            data.save(manager.to_dict(json_data))

    elif reply is 3:
        print(f'Total number of topics = {len(manager.topics)}')
        for i, t in enumerate(manager.topics, start=1):
            print(f'{i}. {t}')
        input('press enter to continue...')

    elif reply is 0:
        print('Thank you for using LabLog.')
        time.sleep(0.2)
        print('Exiting....')
        time.sleep(1.5)
        break