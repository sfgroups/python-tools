from python_tools.fastapi.service_layer.service import Service


class GetTotal:
    def process(self, a, b) -> int:
        return Service.calculate(a, b)
