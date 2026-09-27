from fastapi import FastAPI, Query, HTTPException
from models import MenuResponse, MenuItem
from data import menu_items

app = FastAPI(
    title="Chai Point Menu API",
    description="This is a chai menu fastapi backend",
    version="0.1.0"
)

@app.get("/", tags=["basic"])
def welcome():
    return {
        "message": "Welcome to the fastapi chai menu API"
    }

@app.get("/healthz", tags=["basic"])
def welcome():
    return {
        "message": "Fastapi chai menu is working fine"
    }

@app.get("/menu", response_model=MenuResponse)
def get_menu(category: str | None = Query(None, description="Filter by category")):
    filtered = []
    if category:
        for e in menu_items:
            if e["category"] == category.lower():
                filtered.append(e)
        if not filtered:
            raise HTTPException(status_code=404, detail=f"No item found in the category: {category}")
    else:
        filtered = menu_items
    count = len(filtered)
    return MenuResponse(count=count, items=filtered)

@app.get("/menu/{item_id}", response_model=MenuItem)
def get_menu(item_id: int):
    for e in menu_items:
        if e["id"] == item_id:
            return e
    raise HTTPException(status_code=404, detail=f"No item found with the item id: {item_id}")
