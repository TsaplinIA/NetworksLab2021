from pathlib import Path


def getNonExistentName(file_name):
    parts = file_name.split(".")
    name = parts[0]
    if len(parts) == 1:
        extension = ""
    else:
        extension = "." + parts[1]
    while True:
        path = Path.cwd() / (name + extension)
        if path.exists():
            name += "_new"
        else:
            break
    return name + extension