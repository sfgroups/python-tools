from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json

app = FastAPI()

@dataclass_json
@dataclass
class MyData:
    name: str
    age: int

@dataclass_json
@dataclass
class MyResponse:
    items: list[MyData] = field(default_factory=list)

@app.get("/example")
async def example_endpoint():
    # Creating sample data
    data1 = MyData(name="John", age=25)
    data2 = MyData(name="Alice", age=30)

    # Creating a response with a list of JSON values
    response_data = MyResponse(items=[data1, data2])

    # Returning the FastAPI JSONResponse
    return JSONResponse(content=response_data.to_dict(), media_type="application/json")
