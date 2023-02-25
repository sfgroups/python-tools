from unittest.mock import patch

import pytest

from python_tools.pytest_samples.load_data import slow_load
from python_tools.pytest_samples import load_data


def test_slow_load():
    assert "Data" in slow_load()


def test_slow_load(mocker):
    assert "Data" in slow_load()

    expected = 'mock load'

    def mock_load(self):
        return 'mock load'

    mocker.patch("python_tools.pytest_samples.load_data.DataSet.load_data", mock_load)
    actual = slow_load()
    assert actual == expected


def test_slow_load_01(mocker):
    with mocker.patch("python_tools.pytest_samples.load_data.DataSet.load_data", side_effect=Exception('URLError')):
        with pytest.raises(Exception) as excinfo:
            actual = slow_load()
        assert str(excinfo.value) == 'URLError'


def test_slow_load_04():
    with patch.object(load_data.DataSet, 'load_data', side_effect=Exception('URLError')):
        with pytest.raises(Exception) as excinfo:
            actual = load_data.slow_load()
        assert str(excinfo.value) == 'URLError'


def test_slow_load_05():
    with patch(load_data.DataSet, 'load_data', side_effect=Exception('URLError')):
        with pytest.raises(Exception) as excinfo:
            actual = load_data.slow_load()
        assert str(excinfo.value) == 'URLError'