from python_tools.sample.service import Service


class GetTotal:
    def process(self, a, b) -> int:
        return Service.calculate(a, b)
