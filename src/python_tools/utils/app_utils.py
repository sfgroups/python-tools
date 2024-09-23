from pathlib import Path
class AppUtils:

    @staticmethod
    def find_project_root( current_path: Path = Path(__file__).parent) -> Path:
        # Files that typically indicate the project root
        root_indicators = {"setup.py", "pyproject.toml", "requirements.txt", ".git"}

        # Traverse up the directory tree
        for parent in current_path.resolve().parents:
            if any((parent / indicator).exists() for indicator in root_indicators):
                return parent
        return current_path.resolve()  # Default to the current path if no root is found

if __name__ == '__main__':
    # Usage
    project_root = AppUtils.find_project_root()
    print(f"Project root: {project_root}")
