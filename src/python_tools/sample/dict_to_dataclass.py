import json
from dataclasses import dataclass

from dataclasses_json import dataclass_json

# Sample JSON data
json_data = '''
{
  "name": "John",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "New York"
  },
  "hobbies": ["reading", "coding"]
}
'''


# Define a function to convert nested dictionaries to dataclasses recursively
def dict_to_dataclass(dataclass_type, data):
    fields = dataclass_type.__dataclass_fields__
    kwargs = {
        field_name: dict_to_dataclass(fields[field_name].type, data.get(field_name))
        for field_name in fields
    }
    return dataclass_type(**kwargs)


# Define the main dataclass representing the JSON structure
@dataclass_json
@dataclass
class Person:
    name: str
    age: int
    address: 'Address'
    hobbies: list


@dataclass_json
@dataclass
class Address:
    street: str
    city: str


# Load JSON data into a dictionary
json_dict = json.loads(json_data)

# Convert the dictionary to a dataclass instance
person_instance = dict_to_dataclass(Person, json_dict)

# Now you can work with the dataclass instance as an object
print(person_instance.name)
print(person_instance.age)
print(person_instance.address.street)
print(person_instance.hobbies)
