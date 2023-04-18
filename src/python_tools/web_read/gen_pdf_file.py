import glob
import os
import subprocess
from pathlib import Path


def find_files():
    download_folder = Path(Path.home(), 'Downloads', 'Test')
    files = glob.glob('fmb_*.html', root_dir=download_folder)
    print(files)
    script_dir = Path(Path.home(), "work", "fmb")
    os.chdir(script_dir)
    for file in files:
        file_with_path = Path(download_folder, file)
        pdf_file = str(file_with_path).replace(".html", ".pdf")
        if not Path(pdf_file).exists():
            script = Path(os.getcwd(), "jsscript.js")
            script = "jsscript.js"
            cmd = f"node {script} {file_with_path}"
            print(cmd)
            result = subprocess.run(["node", script, str(file_with_path)], capture_output=True, text=True)
            print(result)
        else:
            print(f"{pdf_file} : already processed")


if __name__ == "__main__":
    find_files()
