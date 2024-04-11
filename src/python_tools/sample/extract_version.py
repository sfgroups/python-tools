from bs4 import BeautifulSoup

# Corrected HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
  <title>My First HTML Page</title>
</head>
<body>
  <h1>Hello, world!</h1>
  <p>This is my first HTML page.</p>
  <p><strong>System Owner</strong> | </p>
  <p><strong>Authorizing Officials</strong> | J |</p>
  <p><strong>Designated Delegates</strong> | J |</p>
  <p><strong>Operational Status</strong> | Draft |</p>

  <h2>1.2 Source Reference</h2>

  <p>| | |
  |--|--|
  |<strong>Template Version</strong> | 2.0 |</p>
</body>
</html>
"""

# Parse the corrected HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find row containing "Template Version" and extract version number
template_version_row = soup.find(text="Template Version").find_parent('p')
version_number = template_version_row.find_all('strong')[-1].next_sibling.strip()

# Print the extracted version number
print(f"Version Number: {version_number}")
