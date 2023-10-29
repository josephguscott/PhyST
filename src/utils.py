def ReadFile(file_path: str) -> None:
    with open(file_path) as file:
            for line in file:
                output = line

    return output

def WriteFile(file_path: str, data_structure: list) -> None:
    with open(file_path, 'a+') as file:
        for line in data_structure:
            file.write(f"{line}")