from fastapi import FastAPI
from models import Product
app = FastAPI()
@app.get("/")
def greet():
    return("Hello world")

products = [
    Product(1,"Phone","Apple Phone",1000,5),
    Product(2,"Lap","Dell Lap",200,50),
    Product(3,"Tab","KIA Phone",20.89,15)
]
@app.get("/products")
def getAllProducts():
    return products