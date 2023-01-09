import json
from unittest.mock import patch, Mock

import pytest


def test_mock_exception():
    mock = Mock()
    mock.a.return_value = 'A'
    assert mock.a() == 'A'
    print(mock.mock_calls)
    mock.a.assert_called()

    def func(n):
        return n + 1

    mock.b.side_effect = func
    assert mock.b(3) == 4

    mock.c.side_effect = ZeroDivisionError("zero")

    with pytest.raises(Exception) as excinfo:
        mock.c()
    assert str(excinfo.value) == 'zero'


def get_json(filename):
    try:
        return json.loads(open(filename).read())
    except (IOError, ValueError):
        return ""


@patch("builtins.open")
def test_get_valid_json(mock_open):
    filename = " not valid.json"
    mock_file = Mock()
    mock_file.read.return_value = '{"foo": "bar"}'
    mock_open.return_value = mock_file

    actual_result = get_json(filename)
    assert {u'foo': u'bar'} == actual_result


@patch("builtins.open")
def test_get_valid_json_exception(mock_open):
    filename = " not valid.json"
    mock_open.side_effect = IOError

    actual_result = get_json(filename)
    assert "" == actual_result


def get_json_ioerror(filename):
    try:
        return json.loads(open(filename).read())
    except (IOError, ValueError):
        return ""


@patch("builtins.open")
def test_get_valid_json_exception(mock_open):
    filename = " not valid.json"
    mock_open.side_effect = IOError

    actual_result = get_json_ioerror(filename)
    assert "" == actual_result
