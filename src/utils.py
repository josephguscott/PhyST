def readFile(file_path):
    with open(file_path) as file:
            for line in file:
                output = line

    return output

def writeFile(file_path, data_structure):
    with open(file_path, 'a+') as file:
        for line in data_structure:
            file.write(f"{line}")