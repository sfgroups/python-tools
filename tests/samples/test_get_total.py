from python_tools.sample.get_total import GetTotal


def test_process():
    assert GetTotal().process(2, 3) == 15
