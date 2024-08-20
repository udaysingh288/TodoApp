from fastapi import FastAPI
import models
from database import engine
from routers import auth,todos,admin
app = FastAPI()

##will only run if todos.db does not exist
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)