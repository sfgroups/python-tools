from unittest.mock import patch, Mock

import pytest

from python_tools.pytest_samples.main import get_response_from_external_api


def test_url_error2():
    mock_query = Mock()
    mock_query.make_request_and_get_response.side_effect = Exception('URLError')
    with pytest.raises(Exception) as excinfo:
        get_response_from_external_api(mock_query)
    assert str(excinfo.value) == 'URLError'


@patch('python_tools.pytest_samples.main.Query')
def test_url_error_01(mocked_query):
    with patch.object(mocked_query, 'make_request_and_get_response', side_effect=Exception('URLError')):
        with pytest.raises(Exception) as excinfo:
            get_response_from_external_api(mocked_query)
        assert str(excinfo.value) == 'URLError'


@patch('python_tools.pytest_samples.main.Query')
def test_url_error(mocked_query):
    with patch.object(mocked_query, 'make_request_and_get_response', side_effect=Exception('URLError')):
        with pytest.raises(Exception) as excinfo:
            get_response_from_external_api(mocked_query)
        assert str(excinfo.value) == 'URLError'

