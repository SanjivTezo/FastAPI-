from fastapi import APIRouter
import httpx

router = APIRouter()

DUMMY_API_URL = "https://dummyjson.com/products"

@router.get("/products")
async def get_products():
    async with httpx.AsyncClient() as client:
        response = await client.get(DUMMY_API_URL)
        response.raise_for_status()
        data = response.json()
        return data["products"]

@router.get("/products/summary")
async def get_product_summaries():
    async with httpx.AsyncClient() as client:
        response = await client.get(DUMMY_API_URL)
        response.raise_for_status()
        data = response.json()
        products = data["products"]

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
