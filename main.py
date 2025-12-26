from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic model
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

# In-memory "database"
products = []

# Create
@app.post("/products/")
def create_product(product: Product):
    products.append(product)
    return {"message": "Product created successfully", "product": product}

# Read all
@app.get("/products/")
def get_products():
    return products

# Read one
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Update
@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return {"message": "Product updated successfully", "product": updated_product}
    raise HTTPException(status_code=404, detail="Product not found")

# Delete
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            deleted_product = products.pop(index)
            return {"message": "Product deleted successfully", "product": deleted_product}
    raise HTTPException(status_code=404, detail="Product not found")
