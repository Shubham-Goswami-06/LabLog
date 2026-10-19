lazy import topic
lazy import data
lazy import os
lazy import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome():
    clear_screen()
    log = data.load()
    print('='*50)
    print(' '*10, f'Welcome to LabLog, {log['Name']}')
    print('='*50)

    print('\n\nSelect an option')
    print(f"1. View all topics\n2. Add a topic\n3. Delete a topic\n4. Search a topic\n5. Change a topic status\n6. View student's details\n0. Quit")

    user_reply = int(input('Enter the option: '))

    match user_reply:
        case 0: quit()
        case 1: show_page()
        case 2: add_page()
        case 3: delete_page()
        case 4: search_page()
        case 5: change_page()
        case 6: filter_page()
        case _: print('Invalid option. Please try again.'); time.sleep(1.5); welcome()

def add_page():
    clear_screen()
    status = ['Complete', 'Incomplete', 'Currently Studying', 'Yet to start']
    print("="*50, f'\nAdd a topic\n', "="*50, '\n\n')
    topic_name = input('Enter the topic name or "#" to go back: ')
    if topic_name == "#":
        welcome()
    print('\nSelect the Status of the topic.')
    for i, s in enumerate(status):
        print(f'{i}. {s}')
    sidx = int(input('Enter the option: '))
    topic.add(topic_name, sidx, status)
    print('Topic Added\n\n')
    print(f'1. Add more topics\n2. Go to Homepage\n0. Quit')
    user_reply = int(input('Enter the option: '))
    match user_reply:
        case 0: quit()
        case 1: add_page()
        case 2: welcome()
        case _: print('Invalid option. Please try again.'); time.sleep(1.5); add_page()



def delete_page():
    clear_screen()
    print("="*50,'\n', ' '*10, f'\nDelete a topic\n', "="*50, '\n\n')
    topic_name = input('Enter the topic name to delete or "#" to go back: ')
    if topic_name == "#":
        welcome()
    topic.delete(topic_name)
    print('Topic deleted.\n')
    print(f'1. Delete more topics\n2. Go to Homepage\n0. Quit')
    user_reply = int(input('Enter the option: '))
    match user_reply:
        case 0: quit()
        case 1: delete_page()
        case 2: welcome()
        case _: print('Invalid option. Please try again.'); time.sleep(1.5); delete_page()

def search_page():
    clear_screen()
    print("="*50,'\n', ' '*10, f'\nSearch a topic\n', "="*50, '\n\n')
    topic_name = input('Enter the topic name to search or "#" to go back: ')
    if topic_name == "#":
        welcome()
    topic.search(topic_name)
    print(f'\n1. Search more topics\n2. Go to Homepage\n0. Quit')
    user_reply = int(input('Enter the option: '))
    match user_reply:
        case 0: quit()
        case 1: search_page()
        case 2: welcome()
        case _: print('Invalid option. Please try again.'); time.sleep(1.5); search_page()

def show_page():
    clear_screen()
    print("="*50,'\n', ' '*10, f'View all topics\n', "="*50, '\n\n')
    topic.show()
    print(f'\n1. Go to Homepage\n0. Quit')
    user_reply = int(input('Enter the option: '))
    match user_reply:
        case 0: quit()
        case 1: welcome()
        case _: print('Invalid option. Please try again.'); time.sleep(1.5); show_page()

def change_page():
    clear_screen()
    print("="*50,'\n', ' '*10, f'\nChange a topic status\n', "="*50, '\n\n')
    topic_name = input('Enter the topic name to change status or "#" to go back: ')
    if topic_name == "#":
        welcome()
    status = ['Complete', 'Incomplete', 'Currently Studying', 'Yet to start']
    print('\nSelect the new Status of the topic.')
    for i, s in enumerate(status):
        print(f'{i}. {s}')
    new_status_index = int(input('Enter the option: '))
    topic.change_status(topic_name, status[new_status_index])
    print('Topic status updated.\n')
    print(f'1. Change more topics\n2. Go to Homepage\n0. Quit')
    user_reply = int(input('Enter the option: '))
    match user_reply:
        case 0: quit()
        case 1: change_page()
        case 2: welcome()
        case _: print('Invalid option. Please try again.'); time.sleep(1.5); change_page()

def filter_page():
    clear_screen()
    print("="*50,'\n', ' '*10, f'\nFilter topics by status\n', "="*50, '\n\n')
    status = ['Complete', 'Incomplete', 'Currently Studying', 'Yet to start']
    print('\nSelect the Status to filter topics.')
    for i, s in enumerate(status):
        print(f'{i}. {s}')
    status_index = int(input('Enter the option: '))
    filtered_topics = topic.filter_by_status(status[status_index])
    if filtered_topics:
        print(f'\nTopics with status "{status[status_index]}":')
        for topic_name, topic_status in filtered_topics.items():
            print(f'- {topic_name}: {topic_status}')
    else:
        print(f'\nNo topics found with status "{status[status_index]}".')
    print(f'\n1. Filter by different status\n2. Go to Homepage\n0. Quit')
    user_reply = int(input('Enter the option: '))
    match user_reply:
        case 0: quit()
        case 1: filter_page()
        case 2: welcome()
        case _: print('Invalid option. Please try again.'); time.sleep(1.5); filter_page()

def quit():
    clear_screen()
    print('Thank you for using LabLog')
    time.sleep(1.5)
    exit()

welcome()