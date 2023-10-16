import unicodedata


def remove_non_printable_chars(input_str):
    # Remove characters with control character category
    printable_chars = [ch for ch in input_str if unicodedata.category(ch)[0] != 'C']
    return ''.join(printable_chars)


# Example usage
input_string = "Hello,\x1bWorld!\n"
clean_string = remove_non_printable_chars(input_string)
print(clean_string)
