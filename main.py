from fastapi import FastAPI
from models import Product
app = FastAPI()
@app.get("/")
def greet():
    return("Hello world")

products = [
    Product(id = 1,name = "Phone",description = "Apple Phone",price = 1000,quantity= 5),
    Product(id = 1,name = "Phone",description = "Apple Phone",price = 1000,quantity= 5),
    Product(id = 1,name = "Phone",description = "Apple Phone",price = 1000,quantity= 5),  
]
@app.get("/products")
def getAllProducts():
    return products