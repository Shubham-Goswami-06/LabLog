lazy import topic
lazy import data
lazy import os
lazy import time
lazy import validate

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

log = data.load()

status_options = ['Complete', 'Currently Studying', 'Not Started']

while True:
    clear_screen()
    print(f"{'='*50}\n{' '*10}Welcome to the LabLog!, {log['Name']}\n{'='*50}\n\n")
    print("1. Add a topic")
    print("2. Delete a topic")
    print("3. Search for a topic")
    print("4. Show all topics")
    print("5. Change topic status")
    print("6. Filter topics by status")
    print("0. Exit")

    choice = input("Enter your choice: ")
    

    if choice == '1':
        clear_screen()
        print(f"{'='*50}\n{' '*15}Add a topic\n{'='*50}\n\n")
        topic_name = validate.valid_topic_name()
        if topic_name=='0': continue
        for i, s in enumerate(status_options, start=1):
            print(f'{i}. {s}')
        
        s = validate.valid_status_selection(len(status_options))
        if s==0: continue
        done = topic.add(topic_name, status_options[s-1], log)
        print(done)
        input("Press Enter to continue...")

    elif choice == '2':
        clear_screen()
        print(f"{'='*50}\n{' '*15}Delete a topic\n{'='*50}\n\n")
        topic_name = input('Enter a topic name or 0 to go to homepage: ')
        if topic_name=='0': continue
        job = topic.delete(topic_name, log)
        print(job)
        input("Press Enter to continue...")

    elif choice == '3':
        clear_screen()
        print(f"{'='*50}\n{' '*15}Search a topic\n{'='*50}\n\n")
        topic_name = input('Enter a topic name or 0 to go to homepage: ')
        if topic_name=='0': continue
        job = topic.search(topic_name, log)
        print(job)
        input("Press Enter to continue...")

    elif choice == '4':
        clear_screen()
        print(f"{'='*50}\n{' '*20}Topics List\n{'='*50}\n\n")
        for i, (topic, status) in enumerate(log['topics'].items(), start=1):
            print(f'{i}. {topic}: {status}', end='\n')
        input("Press Enter to continue...")

    elif choice == '5':
        clear_screen()
        print(f"{'='*50}\n{' '*12}Change a topic's status\n{'='*50}\n\n")
        topic_name = input('Enter a topic name or 0 to go to homepage: ')
        if topic_name=='0': continue
        print(topic.search(topic_name, log), '\n\n')
        for i, s in enumerate(status_options, start=1):
            print(f'{i}. {s}')
        s = validate.valid_status_selection(len(status_options))
        if s==0: continue
        done = topic.change_status(topic_name, status_options[s-1], log)
        print(done)
        input("Press Enter to continue...")


    elif choice == '6':
        clear_screen()
        print(f"{'='*50}\n{' '*12}Filter topics by status\n{'='*50}\n\n")
        for i, s in enumerate(status_options, start=1):
            print(f'{i}. {s}')
        s = validate.valid_status_selection(len(status_options))
        if s==0: continue
        filtered = topic.filter_by_status(status_options[s-1], log)
        print(f'\n\nTopics with status {status_options[s-1]}\n')
        if len(filtered) is not 0:
            for i, t in enumerate(filtered, start=1):
                print(f'{i}. {t}')
        else: print(f'No topic exists with status {status_options[s-1]}')
        input("Press Enter to continue...")

    elif choice == '0':
        print("Exiting...")
        time.sleep(1)
        break

    else:
        clear_screen()
        print("Invalid choice. Please try again.")
        time.sleep(1)