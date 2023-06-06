from fastapi import FastAPI, Body
from typing import Optional, Union
from pydantic import BaseModel

#Data models

class Articles (BaseModel): #Datatypes https://fastapi.tiangolo.com/tutorial/extra-data-types/
    itemId: int
    itemName: str
    itemPrice : float 
    availability : bool = True #valeur par défaut/optionel
    rating: Optional[int]
    
app = FastAPI() #nom variable pour server

@app.get("/")  
async def root():
    return {"message": "Est ce que c'est bon pour vous ?"}

@app.get("/articles")
async def get_articles():
    return {
    "articles":
    [
        {"itemId": "item_id", "itemName" : "item_name","price_id": "prices"},
        {"itemId": "item_id1", "itemName" : "item_name1", "itemPrice": "prices1"},
        {"itemId": "item_id2", "itemName" : "item_name2", "itemPrice": "prices2"},
        {"itemId": "item_id3", "itemName" : "item_name3", "itemPrice": "prices3"} 
    ],
    "limit": 10,
    "total": 2,
    "skip" : 0 
    }   
articles = [
        {"itemId": "item_id", "itemName" : "item_name","price_id": "prices"},
        {"itemId": "item_id1", "itemName" : "item_name1", "itemPrice": "prices1"},
        {"itemId": "item_id2", "itemName" : "item_name2", "itemPrice": "prices2"},
        {"itemId": "item_id3", "itemName" : "item_name3", "itemPrice": "prices3"} 
    ]         
@app.get("/articles/{item_id}")  
async def articles_items(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/articles")
async def create_article(payload: Articles):
    print(payload.itemName)
    articles.append(payload.dict())
    return {
        "message": f"{payload.itemName} added successfully"
    }