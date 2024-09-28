def get_file_content(filename):
    code = []
    with open(filename, "r") as file:
        for i in file.readlines():
            code.append(i.rstrip())
    return code