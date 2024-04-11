import re


def remove_non_alphanumeric(text):
    """Removes non-alphanumeric characters from a string.

    Args:
        text (str): The input string.

    Returns:
        str: The string with only alphanumeric characters remaining.
    """

    return re.sub(r"[^\w]", "", text)  # Use a regular expression for efficiency


def compare_strings(str1, str2):
    """Compares two strings after removing non-alphanumeric characters.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        bool: True if the strings are equal after filtering, False otherwise.
    """

    cleaned_str1 = remove_non_alphanumeric(str1.lower())
    cleaned_str2 = remove_non_alphanumeric(str2.lower())
    return cleaned_str1 == cleaned_str2

# Example usage
string1 = "Hello, world!"
string2 = "Hello world"
if compare_strings(string1, string2):
    print("The strings match after removing non-alphanumeric characters.")
else:
    print("The strings do not match after removing non-alphanumeric characters.")
