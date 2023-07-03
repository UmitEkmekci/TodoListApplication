from fastapi import FastAPI, Depends, Request, Form, status
import uvicorn
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
 
from sqlalchemy.orm import Session
 
from dbfiles import models
from dbfiles import dependencies

 
templates = Jinja2Templates(directory="templates")
 
app = FastAPI()
 
 

 
@app.get("/")
def home(request: Request, db: Session = Depends(dependencies.get_db)):
    todos = db.query(models.Todo).all()
    return templates.TemplateResponse("index.html",
                                      {"request": request, "todo_list": todos})
 
@app.post("/add")
def add(request: Request, title: str = Form(...), db: Session = Depends(dependencies.get_db)):
    new_todo = models.Todo(title=title)
    print(type(title))
    db.add(new_todo)
    db.commit()
 
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
 