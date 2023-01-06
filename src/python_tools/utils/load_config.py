from pathlib import Path


def get_value(key: str) -> str:
    filename = Path(Path.home(), "config.txt")
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith(key):
                return line.split("=")[1]

    return None


if __name__ == "__main__":
    get_value("USERNAME")
