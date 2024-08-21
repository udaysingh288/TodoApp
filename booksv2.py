from fastapi import FastAPI,Body
import json


app =FastAPI()
# class BOOK:
#     def __init__(self,id,title,author,description,rating):
        
BOOKS =[]
@app.get("/books/")
async def read_all_books():
    return BOOKS 
