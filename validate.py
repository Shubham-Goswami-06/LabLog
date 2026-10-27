from status import Status
lazy import time
import ui

def valid_topic_name():
    while True:
        topic_name = input("Enter the topic name or 0 to go to homepage: ").strip()
        if topic_name == '':
            print("Topic name can't be empty. Please! try again")
        else: return topic_name

def valid_status(status_list: list[str]) -> Status:
    for i, st in enumerate(status_list, start=1):
        print(f'{i}. {st}')
    while True:
        try:
            s = int(input("Select a Status: "))
            if s in range(1,4):
                return Status(status_list[s-1])
            else: raise ValueError
        except ValueError:
            print("Invalid option. Please! try again")
            time.sleep(1.5)
            ui.clear_last_lines(2)