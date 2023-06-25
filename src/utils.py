def readFile(file_path: str):
    with open(file_path) as file:
            for line in file:
                output = line

    return output

def writeFile(file_path: str, data_structure: list):
    with open(file_path, 'a+') as file:
        for line in data_structure:
            file.write(f"{line}")