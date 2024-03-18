from bs4 import BeautifulSoup

# HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My HTML Template</title>
</head>
<body>
    <h1> sample code</h1>
    bleow is the text file
    <h2> Source Information</h2>
        <strong>Template version: 20</strong>

</body>
</html>
"""

# Parse HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find h2 tag with text 'Source Information'
h2_tag = soup.find('h2', text=' Source Information')

# Extract template version value
if h2_tag:
    strong_tag = h2_tag.find_next_sibling('strong')
    if strong_tag:
        version_text = strong_tag.get_text()
        template_version = version_text.split(':')[-1].strip()
        print("Template Version:", template_version)
    else:
        print("No template version found.")
else:
    print("No 'Source Information' found.")
