from python_tools.pytest_samples.slow import DataSet


def slow_load():
    dataset = DataSet()
    return dataset.load_data()
