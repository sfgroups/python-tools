from unittest.mock import Mock

from python_tools.pytest_samples.order import Order


def test_order_is_filled():
    # setup - data
    order = Order('Talisker', 50)
    warehouse = Mock()

    # setup - expectations
    warehouse.has_inventory.return_value = True
    warehouse.remove.return_value = None

    # exercise
    order.fill(warehouse)

    # verify
    assert order.is_filled()


def test_order_is_not_filled():
    # setup - data
    order = Order('Talisker', 50)
    warehouse = Mock()

    # setup - expectations
    warehouse.has_inventory.return_value = False

    # exercise
    order.fill(warehouse)
    # verify
    assert not order.is_filled()
