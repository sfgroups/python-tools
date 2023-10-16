import uvicorn
from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "Year 12"
    }
}


@app.get("/")
def index():
    return {"name": "First Data from fastapi"}


@app.get("/get-student/{student_id}")
async def get_student(student_id: int = Path(title="The ID of the student you want to view ")):
    return students[student_id]


if __name__ == "__main__":
    uvicorn.run("myapi:app", host="0.0.0.0", port=8000, reload=True)
