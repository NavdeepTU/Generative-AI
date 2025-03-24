from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = "navdeep" # seting default value as "navdeep"
    age: Optional[int] = None # optinal and default value None
    email: EmailStr # data type for builtin validation of email in pydantic
    cgpa: float = Field(gt=0, lt=10, default=5, description="A decimal value representing the cgpa of the student") # applying constraint and default value, same as Annotated in TypedDict
    # can also add regular expressions for phone number 


new_student = {"name": "nitish",  # cannot be integer
               "age": "32",  # data type coercing (if possible)
               "email": "abc@gmail.com",
               "cgpa": 8,
               } 

student = Student(**new_student)

print(student) # pydantic object

student_dict = dict(student) # converting to dict

print(student_dict["age"])

student_json = student.model_dump_json() # converting to json

print(student_json)

# {"name":"nitish","age":32,"email":"abc@gmail.com","cgpa":8.0}