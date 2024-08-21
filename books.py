from fastapi import FastAPI

app = FastAPI()
BOOKS = [
    {'title':'A','author':'XTY'},
    {'XA':'SSFA','ASF':'ASFGAS'}
]
@app.get("/books")
async def new_func():
    return BOOKS