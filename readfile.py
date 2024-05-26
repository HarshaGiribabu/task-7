def content_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of the file '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
filename = "2024-05-25_17-37-24.txt"
content_file(filename)
