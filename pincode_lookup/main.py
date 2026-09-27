from fastapi import FastAPI, Query, HTTPException
from models import PincodeResponse, PincodeItem
from data import pincode_items

app = FastAPI(
    title="Pincode Lookup API",
    description="A FastAPI backend to lookup Indian pincodes by area, city, and state",
    version="0.1.0"
)

@app.get("/", tags=["basic"])
def welcome():
    return {
        "message": "Welcome to the Pincode Lookup API"
    }

@app.get("/healthz", tags=["basic"])
def healthcheck():
    return {
        "message": "Pincode Lookup API is working fine"
    }

@app.get("/pincodes", response_model=PincodeResponse, tags=["pincodes"])
def get_pincodes(
    city: str | None = Query(None, description="Filter by city"),
    state: str | None = Query(None, description="Filter by state")
):
    filtered = list(pincode_items.values())

    if city:
        filtered = [e for e in filtered if e["city"].lower() == city.lower()]
        if not filtered:
            raise HTTPException(status_code=404, detail=f"No pincode found for city: {city}")

    if state:
        filtered = [e for e in filtered if e["state"].lower() == state.lower()]
        if not filtered:
            raise HTTPException(status_code=404, detail=f"No pincode found for state: {state}")

    return PincodeResponse(count=len(filtered), items=filtered)

@app.get("/pincodes/{pincode}", response_model=PincodeItem, tags=["pincodes"])
def get_pincode(pincode: str):
    if pincode not in pincode_items:
        raise HTTPException(status_code=404, detail=f"No data found for pincode: {pincode}")
    return pincode_items[pincode]
