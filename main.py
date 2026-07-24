from fastapi import FastAPI
from models import Product
app = FastAPI()
@app.get("/")
def greet():
    return("Hello world")

products = [
    Product(id = 1,name = "Phone",description = "Apple Phone",price = 1000,quantity= 5),
    Product(id = 2,name = "Lap",description = "Apple Phone",price = 1000,quantity= 5),
    Product(id = 3,name = "Tab",description = "Apple Phone",price = 1000,quantity= 5),  
]
#GET
@app.get("/products")
def getAllProducts():
    return products
#GET BY ID
@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return("Product Not Found")
#ADD
@app.post("/product")
def add_products(product:Product):
    products.append(product)
    return(product)
#UPDATE
@app.put("/product")
def update_product(id:int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product added successfully"
    return "No product found"
#DELETE
@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product delete successfully"
    return "No product found"