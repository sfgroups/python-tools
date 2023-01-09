from python_tools.pytest_samples.slow import DataSet


def slow_load():
    dataset = DataSet()
    return dataset.load_data()


def slow_load_ex():
    try:
        dataset = DataSet()
        return dataset.load_data()
    except Exception as e:
        raise e

