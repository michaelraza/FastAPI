from fastapi import FastAPI
app = FastAPI() #nom variable pour server

@app.get("/")  
async def root():
    return {"message": "Est ce que c'est bon pour vous ?"}