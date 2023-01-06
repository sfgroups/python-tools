from python_tools.pytest_samples.load_data import slow_load


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
