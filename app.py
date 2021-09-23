from fastapi import FastAPI
from pydantic import BaseModel


from worker import add

app = FastAPI()

class Numbers(BaseModel):
    x : float
    y : float


@app.post('/add')
def add_to_queue(n: Numbers):
    add.delay(n.x, n.y)


