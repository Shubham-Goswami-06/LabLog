import time

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
    return s