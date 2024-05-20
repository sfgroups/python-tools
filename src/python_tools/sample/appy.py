from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Mount static files for serving CSS and JS
#app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML form template with Bootstrap and validation
form_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Form</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
</head>
<body>
    <div class="container mt-5">
        <h1 class="mb-4">Enter your details</h1>
        <form id="dataForm" action="/submit" method="post" onsubmit="return validateForm()">
            <div class="form-group">
                <label for="field1">Field 1:</label>
                <input type="text" class="form-control" id="field1" name="field1">
                <div class="invalid-feedback">Field 1 must be at least 3 characters long.</div>
            </div>
            <div class="form-group">
                <label for="field2">Field 2:</label>
                <input type="text" class="form-control" id="field2" name="field2">
                <div class="invalid-feedback">Field 2 must be at least 3 characters long.</div>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
    </div>
    <script>
        function validateForm() {
            var isValid = true;
            $('.form-control').each(function() {
                if ($(this).val().length < 3) {
                    $(this).addClass('is-invalid');
                    isValid = false;
                } else {
                    $(this).removeClass('is-invalid');
                }
            });
            return isValid;
        }
    </script>
</body>
</html>
"""

# Response template with Bootstrap and jQuery
response_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Form Response</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
    <style>
        .code-block {
            border: 1px solid blue;
            padding: 10px;
            background-color: #f8f9fa;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <h1 class="mb-4">Form Submitted</h1>
        <div class="code-block">
            <code>Field 1: {{ field1 }}</code><br>
            <code>Field 2: {{ field2 }}</code><br>
            <code>Some template text here...</code>
        </div>
        <button id="copyButton" class="btn btn-secondary mt-3">Copy to Clipboard</button>
    </div>
    <script>
        $(document).ready(function() {
            $('#copyButton').click(function() {
                var text = "Field 1: {{ field1 }}\\nField 2: {{ field2 }}\\nSome template text here...";
                var tempInput = $('<input>');
                $('body').append(tempInput);
                tempInput.val(text).select();
                document.execCommand('copy');
                tempInput.remove();
                alert('Copied to clipboard');
            });
        });
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
async def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
async def submit(request: Request, field1: str = Form(...), field2: str = Form(...)):
    return templates.TemplateResponse("response.html", {"request": request, "field1": field1, "field2": field2})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
