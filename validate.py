import time
import ui

def valid_status_selection(size: int) -> int:
    while True:
        try:
            s = int(input('Select a status or 0 to go to homepage: '))
            if 0<=s<=size: break
            else:
                print('Invalid option please try again')
                time.sleep(1)
        except ValueError:
            print('Invalid option please try again')
            time.sleep(1)
        ui.clear_last_lines(2)
    return s

def valid_topic_name():
    while True:
        topic_name = input("Enter the topic name or 0 to go to homepage: ")
        topic_name.strip()
        if topic_name == None:
            print("Topic name can't be empty. Please! try again")
        else: return topic_name