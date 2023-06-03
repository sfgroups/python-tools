import asyncio
import subprocess

import uvicorn
from fastapi import BackgroundTasks, FastAPI
from pyppeteer import launch
from weasyprint import HTML

app = FastAPI()


def convert_html_to_pdf(html_content: str, output_file: str):
    print("String conversion")
    html = HTML(string=html_content)
    pdf = html.write_pdf(output_file)
    print("PDF conversion complete")


def convert_html_file_to_pdf(html_file: str, output_file: str):
    print("String conversion")
    html = HTML(string=html_file)
    pdf = html.write_pdf(output_file)
    print("PDF conversion complete")


@app.get("/file")
async def start(background_tasks: BackgroundTasks):
    background_tasks.add_task(convert_html_to_pdf, html_content="sample.html", output_file="sample.pdf")
    return {"status": "ok"}


@app.get("/start")
async def start(background_tasks: BackgroundTasks):
    background_tasks.add_task(convert_html_to_pdf, html_content="<h1>Hello World</h1>", output_file="hello.pdf")
    return {"status": "ok"}


@app.get("/pyconvert")
async def pyconvert(background_tasks: BackgroundTasks):
    background_tasks.add_task(call_another_script)
    return {"status": "ok"}


@app.post("/convert")
async def convert_to_pdf(background_tasks: BackgroundTasks, html_content: str):
    output_file = "output.pdf"
    background_tasks.add_task(convert_html_to_pdf, html_content, output_file)
    return {"message": "Conversion task started"}


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


def call_convert():
    print("String conversion")
    html_file = "/app/src/python_tools/fastapi/sample.html"
    pdf_file = html_file.replace(".html", ".pdf")
    asyncio.get_event_loop().run_until_complete(convert_html_to_pdf(html_file, pdf_file))
    print("PDF conversion complete")

def call_another_script():
    command = ['/app/venv/bin/python', '/app/src/python_tools/fastapi/pyp-html2pdf.py', 'arg1', 'arg2']
    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)

    # Check the result
    if result.returncode == 0:
        # The script was executed successfully
        print("Script executed successfully.")
        print("Output:")
        print(result.stdout)
    else:
        # An error occurred while running the script
        print("Error executing the script.")
        print("Error message:")
        print(result.stderr)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
