from storage import Storage
lazy import time

def create_new_user() -> dict:
    json_data: dict[str, str | dict] = {'__version__': 'v0.3'}
    while True:
        name = input('Enter your name: ').strip()
        if name:
            json_data['name'] = name
            break
        else: 
            print('Please enter a valid name')
            time.sleep(1)
    json_data['topics'] = {}
    return json_data