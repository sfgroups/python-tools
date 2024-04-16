import markdown

# Function to add "INSERT HERE" text below the matched H2 tag
def add_insert_text(md_file, input_string):
    with open(md_file, 'r') as file:
        markdown_content = file.read()

    # Parse the Markdown content
    md = markdown.Markdown(extensions=['markdown.extensions.headerid', 'markdown.extensions.extra'])

    # Render the Markdown content
    md.convert(markdown_content)

    # Find all H2 elements and add "INSERT HERE" text below the matching H2 tag
    modified_content = ""
    for line in markdown_content.splitlines():
        if line.startswith("## "):
            heading_text = line[3:]
            if input_string.lower() in heading_text.lower():
                modified_content += line + "\nINSERT HERE\n\n"
            else:
                modified_content += line + "\n\n"
        else:
            modified_content += line + "\n"

    # Write the modified content back to the file
    with open(md_file, 'w') as file:
        file.write(modified_content)

# Example usage
if __name__ == "__main__":
    md_file = "sample.md"  # Replace with the path to your Markdown file
    input_string = "Heading 2"  # Replace with the string you want to match against H2 headings
    add_insert_text(md_file, input_string)
    print("Modified Markdown file created successfully.")
