import datetime
def timestamp():
    curnt_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{curnt_timestamp}.txt"
    with open(filename, 'w') as file:
        file.write(curnt_timestamp)
    print(f"File '{filename}' created with content: {curnt_timestamp}")
timestamp()
