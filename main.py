from fastapi import FastAPI, Body, HTTPException, Response, status
from typing import Optional, Union
from pydantic import BaseModel

app = FastAPI()

# Data models

class Articles(BaseModel):
    itemId: int
    itemName: str
    itemPrice: float
    availability: bool = True
    rating: Optional[int]

class ProductRouter:
    articles = [
        {"itemId": "item_id", "itemName": "item_name", "price_id": "prices"},
        {"itemId": "item_id1", "itemName": "item_name1", "itemPrice": "prices1"},
        {"itemId": "item_id2", "itemName": "item_name2", "itemPrice": "prices2"},
        {"itemId": "item_id3", "itemName": "item_name3", "itemPrice": "prices3"}
    ]

    @app.get("/products")
    async def get_articles(self):
        return {
            "articles": self.articles,
            "limit": 10,
            "total": 2,
            "skip": 0
        }

    @app.get("/products/{itemId}")
    async def get_item(self, itemId: int, response: Response):
        try:
            corresponding_product = self.articles[itemId - 1]
            return corresponding_product
        except:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="Article not found"
            )

    @app.post("/products")
    async def create_article(self, payload: Articles, response: Response):
        print(payload.itemName)
        self.articles.append(payload.dict())
        response.status_code = status.HTTP_201_CREATED
        return {
            "message": f"{payload.itemName} added successfully"
        }

    @app.delete("/products/{itemId}")
    async def delete_item(self, itemId: int, response: Response):
        try:
            self.articles.pop(itemId - 1)
            response.status_code = status.HTTP_204_NO_CONTENT
        except:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="Item not found"
            )

    @app.put("/products/{itemId}")
    async def replace_item(self, itemId: int, payload: Articles, response: Response):
        try:
            self.articles[itemId - 1] = payload.dict()
            return {"message": f"Item successfully updated: {payload.itemName}"}
        except:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="Item not found"
            )

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserRouter:
    user = [
        {"userId": "user_id1"},
        {"userId": "user_id2"},
        {"userId": "user_id3"}
    ]

    @app.get("/users")
    async def get_user(self):
        return {"user": self.user}

    @app.get("/users/{userId}")
    async def get_user_byID(self, userId: int, response: Response):
        try:
            corresponding_user = self.user[userId - 1]
            return corresponding_user
        except:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

    @app.post("/users")
    async def create_user(self, payload: User, response: Response):
        print(payload.username)
        self.user.append(payload.dict())
        response.status_code = status.HTTP
        
class Transactions(BaseModel):
    transactionId: int
    itemId: int
    quantity: int
    amount: float
class TransactionRouter:
    transactions = [
        {"transactionId": 1, "itemId": 1, "quantity": 2, "amount": 10.0},
        {"transactionId": 2, "itemId": 2, "quantity": 1, "amount": 5.0},
        {"transactionId": 3, "itemId": 3, "quantity": 3, "amount": 20.0}
    ]

    @app.get("/transactions")
    async def get_transactions(self):
        return {"transactions": self.transactions}

    @app.get("/transactions/{transactionId}")
    async def get_transaction(self, transactionId: int, response: Response):
        try:
            corresponding_transaction = self.transactions[transactionId - 1]
            return corresponding_transaction
        except:
            raise HTTPException(
                status.HTTP_404_NOT_FOUND,
                detail="Transaction not found"
            )

    @app.post("/transactions")
    async def create_transaction(self, payload: Transactions, response: Response):
        print(payload.transactionId)
        self.transactions.append(payload.dict())
        response.status_code = status.HTTP_201_CREATED
