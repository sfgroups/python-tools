from python_tools.sample.service import Service


class GetTotal:
    def process(self, a, b) -> int:
        return Service.calculate(a, b)


if __name__ == '__main__':
    obj = GetTotal()
    print(obj.process(5, 3))
