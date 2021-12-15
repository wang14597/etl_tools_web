from pydantic import BaseModel


class HelloWorld(BaseModel):
    content: str


class Jobs(BaseModel):
    jobs: list


