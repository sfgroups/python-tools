# config.py

import json

class SingletonConfig:
    _instance = None
    _config = None

    def __new__(cls, config_path="config.json"):
        if cls._instance is None:
            cls._instance = super(SingletonConfig, cls).__new__(cls)
            cls._config = cls._load_config(config_path)
        return cls._instance

    @classmethod
    def _load_config(cls, config_path):
        with open(config_path, "r") as config_file:
            return json.load(config_file)

    @property
    def database_url(self):
        return self._config.get("database_url")

    @property
    def max_items_per_page(self):
        return self._config.get("max_items_per_page")
