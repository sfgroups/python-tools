from python_tools.sample.string_compare import  remove_non_alphanumeric, compare_strings

def test_remove_non_alphanumeric():
    assert remove_non_alphanumeric("Hello, World!") == "HelloWorld"
    assert remove_non_alphanumeric("42") == "42"
    assert remove_non_alphanumeric("%$#") == ""

def test_compare_strings():
    assert compare_strings("Hello, World!", "hElLo WoRlD") == True
    assert compare_strings("Python!", "PyTh0n") == False
    assert compare_strings("Test123", "Test  456") == False