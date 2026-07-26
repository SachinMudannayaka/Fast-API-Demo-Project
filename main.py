from fastapi import Depends, FastAPI
from models import Product
from database import SessionLocal, engine
import database_models
app = FastAPI()
from sqlalchemy.orm import session

database_models.Base.metadata.create_all(bind = engine)

@app.get("/")
def greet():
    return("Hello world")

products = [
    Product(id = 1,name = "Phone",description = "Apple Phone",price = 1000,quantity= 5),
    Product(id = 2,name = "Lap",description = "Apple Phone",price = 1000,quantity= 5),
    Product(id = 3,name = "Tab",description = "Apple Phone",price = 1000,quantity= 5),  
]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:    
        db.close()

def init_db():
    db = SessionLocal()
    count = db.query(database_models.Product).count
    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))
        db.commit()

init_db()    
#GET
@app.get("/products")
def getAllProducts(db:session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    return db_products

#GET BY ID
@app.get("/product/{id}")
def get_product_by_id(id: int,db:session = Depends(get_db)):
    # for product in products:
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product.id == id:
        return db_product
    return("Product Not Found")
#ADD
@app.post("/product")
def add_products(product:Product,db:session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return(product)

#UPDATE
@app.put("/product")
def update_product(id:int, product: Product,db:session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return("Product UPDATED")
    else:
        return "NO PRODUCT"    
#DELETE
@app.delete("/product",)
def delete_product(id:int,db:session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    else:
        return("NOT FOUND")    
