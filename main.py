import os


def get_contents_of_one_file(file_content):
    file_values = []
    for row in file_content.split("\n")[1:-1]:
        file_values.append(row.split(","))

    return file_values


def read_files():
    file_names = os.listdir("weatherfiles")

    # file_reader = open("main.py", "r")
    # file_content = file_reader.read()
    # file_reader.close()

    file_values = []

    for file_name in file_names:
        with open(f"weatherfiles/{file_name}", "r") as file_reader:
            file_content = file_reader.read()

            file_values += get_contents_of_one_file(file_content)

    return file_values


file_values = read_files()

for file_value in file_values:
    print(file_value)
