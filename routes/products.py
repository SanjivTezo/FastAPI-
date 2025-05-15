from fastapi import APIRouter
import httpx

router = APIRouter()

DUMMY_API_URL = "https://dummyjson.com/products"

# helper function to fetch data from the dummy API
async def fetch_product():
    async with httpx.AsyncClient() as client:
        response = await client.get(DUMMY_API_URL)
        response.raise_for_status()
        return response.json()
    
    
@router.get("/products")
async def get_products():
    return await fetch_product()

@router.get("/products/summary")
async def get_product_summaries():
    
    data = await fetch_product()
    # products = data["products"]
    products = data.get("products", [])  # safer access
    
    summary = [
            {
                "id": product["id"],
                "title": product["title"],
                "price": product["price"],
                "rating": product["rating"],
                "thumbnail": product["thumbnail"]
            }
            for product in products
        ]
    return summary
