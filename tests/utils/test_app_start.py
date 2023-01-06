from src.python_tools.utils.app_start import AppStart


def test_connect():
    app=AppStart()
    assert app.connect() == "appuser"

