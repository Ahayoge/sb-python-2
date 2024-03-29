import os

def generateErrorLog(path: str) -> iter:
    with open(path, "r", encoding="UTF-8") as log_file:
        for line in log_file:
            if ("ERROR" in line): yield line.rstrip()

with open("errors.txt", "w") as file:
    for i in generateErrorLog(os.path.join("test.txt")):
        file.write(f"{i}\n")