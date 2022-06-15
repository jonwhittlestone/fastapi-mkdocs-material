from typing import Union
from starlette.templating import Jinja2Templates

from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates("templates")
app.mount("/static", StaticFiles(directory="templates/static"), name="static")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/welcome")
def welcome(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
