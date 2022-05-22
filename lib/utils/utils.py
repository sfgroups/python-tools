from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent


def get_data_dir():
    return Path(get_project_root(), "data")


def _main():
    print(get_project_root())


if __name__ == "__main__":
    # pass
    _main()
