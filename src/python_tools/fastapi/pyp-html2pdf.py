import asyncio

from pyppeteer import launch


async def convert_html_to_pdf(html_file, pdf_file):
    browser = await launch(headless=True, ignoreHTTPSErrors=True, args=['--no-sandbox'], dumpio=True)
    page = await browser.newPage()

    # Set the content of the page to the HTML file
    with open(html_file, 'r') as f:
        html_content = f.read()
    await page.setContent(html_content)

    # Generate the PDF
    await page.pdf({'path': pdf_file})

    # Close the browser
    await browser.close()


def call_html_to_pdf():
    html_file = "sample.html"
    generate_html_file(html_file)
    pdf_file = html_file.replace(".html", ".pdf")
    asyncio.get_event_loop().run_until_complete(convert_html_to_pdf(html_file, pdf_file))


def generate_html_file(file_name):
    html = '''
    <html>
    <head>
        <style>
            h1 {
                color: blue;
            }

            h2 {
                color: green;
            }

            table {
                border-collapse: collapse;
            }

            table, th, td {
                border: 1px solid black;
            }

            td {
                padding: 5px;
            }
            .red {
                background-color: red;
            }
            
            .blue {
                background-color: blue;
            }
            
            .green {
                background-color: green;
            }
            
            .yellow {
                background-color: yellow;
            }
            
            .pink {
                background-color: pink;
            }
        </style>
    </head>
    <body>
        <h1>Heading 1</h1>
        <table>
            <tr>
                <th>Column 1</th>
                <th>Column 2</th>
                <th>Column 3</th>
            </tr>
            <tr>
                <td style="background-color: yellow;">Row 1, Cell 1</td>
                <td style="background-color: orange;">Row 1, Cell 2</td>
                <td style="background-color: pink;">Row 1, Cell 3</td>
            </tr>
            <tr>
                <td style="background-color: lightblue;">Row 2, Cell 1</td>
                <td style="background-color: lightgreen;">Row 2, Cell 2</td>
                <td style="background-color: lightyellow;">Row 2, Cell 3</td>
            </tr>
        </table>

        <h2>Heading 2</h2>
        <table>
            <tr>
                <th>Column 1</th>
                <th>Column 2</th>
                <th>Column 3</th>
            </tr>
            <tr>
                <td style="background-color: violet;">Row 1, Cell 1</td>
                <td style="background-color: aqua;">Row 1, Cell 2</td>
                <td style="background-color: coral;">Row 1, Cell 3</td>
            </tr>
            <tr>
                <td style="background-color: lavender;">Row 2, Cell 1</td>
                <td style="background-color: thistle;">Row 2, Cell 2</td>
                <td style="background-color: silver;">Row 2, Cell 3</td>
            </tr>
        </table>

        <h1>Sample HTML Table</h1>
  <table>
    <thead>
      <tr>
        <th>Name</th>
        <th>Age</th>
        <th>City</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>John Doe</td>
        <td>30</td>
        <td>New York</td>
      </tr>
      <tr>
        <td>Jane Smith</td>
        <td>25</td>
        <td>London</td>
      </tr>
      <tr>
        <td>Bob Johnson</td>
        <td>40</td>
        <td>Paris</td>
      </tr>
    </tbody>
  </table>
   <h1>Heading 1</h1>
        <table>
            <tr>
                <th>Table Header 1</th>
                <th>Table Header 2</th>
            </tr>
            <tr>
                <td><a href="https://www.example.com">Link 1</a></td>
                <td><a href="https://www.example.com">Link 2</a></td>
            </tr>
            <tr>
                <td><a href="https://www.example.com">Link 3</a></td>
                <td><a href="https://www.example.com">Link 4</a></td>
            </tr>
        </table>
        <h2>Heading 2</h2>
        <table>
            <tr>
                <th>Table Header 3</th>
                <th>Table Header 4</th>
            </tr>
            <tr>
                <td class="red"><a href="https://www.example.com">Link 5</a></td>
                <td class="blue"><a href="https://www.example.com">Link 6</a></td>
            </tr>
            <tr>
                <td class="green"><a href="https://www.example.com">Link 7</a></td>
                <td class="yellow"><a href="https://www.example.com">Link 8</a></td>
            </tr>
            <tr>
                <td class="pink"><a href="https://www.example.com">Link 9</a></td>
                <td><a href="https://www.example.com">Link 10</a></td>
            </tr>
        </table>
    </body>
    </html>
    '''

    with open(file_name, 'w') as file:
        file.write(html)


if __name__ == "__main__":
    call_html_to_pdf()
