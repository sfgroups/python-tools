def test_01():
    a = {'name': 'abcd'}
    b = a
    c = a.copy()
    a['name'] = 'xyz'
    print(b['name'], c['name'])


if __name__ == "__main__":
    test_01()
