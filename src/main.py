from typing import Union
from starlette.templating import Jinja2Templates

from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates("tech-docs")
app.mount("/assets", StaticFiles(directory="tech-docs/assets"), name="assets")


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/tech-docs/{file_path:path}")
def tech_docs(request: Request, file_path: str):
    return templates.TemplateResponse(f"{file_path}", {"request": request})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
