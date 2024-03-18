from pathlib import Path


class WebMessage:
    message = "welcome to the Web"

    def return_text(self):
        return f"{Path.cwd()} {self.message}"

