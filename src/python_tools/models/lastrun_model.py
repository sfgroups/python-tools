import json
from dataclasses import field
from pathlib import Path

from dataclasses_json import dataclass_json, LetterCase

from python_tools.db.app_model import LastRun
from python_tools.utils.app_utils import AppUtils


@dataclass_json(letter_case=LetterCase.SNAKE)
class AppLastRun(LastRun):
  pass


@dataclass_json(letter_case=LetterCase.SNAKE)
class AppLastRunList:
    records: list[AppLastRun] = field(default_factory=list)

def add_json_data():

    filename_path = Path(AppUtils.find_project_root(), "src", "python_tools", "data", "json-data.json")
    with open(filename_path, "r") as f:
        data = json.load(f)

    print(data)

    al = AppLastRunList.from_dict(data)
    print(al)


if __name__ == '__main__':
    add_json_data()