
from typing import Annotated
from pydantic import BaseModel,Field
from fastapi import FastAPI,Depends,status,Path,HTTPException
import models
from database import SessionLocal
from models import Todos
from database import engine
from sqlalchemy.orm import Session

app = FastAPI()

##will only run if todos.db does not exist
models.Base.metadata.create_all(bind=engine)


# @app.get("/t")

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

class TodoRequest(BaseModel):
    title:str=Field(min_length=3)
    description:str=Field(min_length=3,max_length=100)
    priority:int=Field(gt=0,lt=6)
    complete:bool






###read all data from database table
@app.get("/",status_code=status.HTTP_200_OK)
async def read_all(db:db_dependency):
    return db.query(Todos).all()


##fetch by id
@app.get("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def read_todo(db:db_dependency,todo_id:int=Path(gt=0)):
    todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail = 'Todo not found')




###using pydantic class with validation create new object inserted to todos db
@app.post("/todo",status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency,todo_request:TodoRequest):
    todo_model = Todos(**todo_request.model_dump())

    db.add(todo_model)
    db.commit()

###update request

@app.put("/todo/{todo_id}",status_code=status.HTTP_200_OK)
async def update_todo(db:db_dependency,todo_id:int,todo_request:TodoRequest):
    todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail="to do not found")
    todo_model.title=todo_request.title
    todo_model.description=todo_request.description
    todo_model.priority=todo_request.priority
    todo_model.complete=todo_request.complete

    db.add(todo_model)
    db.commit()

@app.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todo_id:int=Path(gt=0)):
    todo_model=db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail="to do not found")
    db.query(Todos).filter(Todos.id==todo_id).delete()
    db.commit()
