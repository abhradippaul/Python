from fastapi import FastAPI
from exceptions import PinCodeNotFoundError, pincode_not_found_handler, InvalidPinCodeError, invalid_pincode_handler
from models import LocationResponse, BulkRequest, BulkResponse
from data import pincode_items

app = FastAPI(
    title="Pincode Lookup API",
    description="A FastAPI backend to lookup Indian pincodes by area, city, and state",
    version="0.1.0"
)

app.add_exception_handler(PinCodeNotFoundError, pincode_not_found_handler)
app.add_exception_handler(InvalidPinCodeError, invalid_pincode_handler)


@app.get("/", tags=["basic"])
def welcome():
    return {"message": "Welcome to the Pincode Lookup API"}


@app.get("/healthz", tags=["basic"])
def healthcheck():
    return {"message": "Pincode Lookup API is working fine"}


@app.get("/pincode/{pincode}", response_model=LocationResponse, tags=["pincodes"])
def lookup_pincode(pincode: str):
    if len(pincode) != 6 or not pincode.isdigit():
        raise InvalidPinCodeError(pincode, "Must be exactly 6 digits")
    if pincode not in pincode_items:
        raise PinCodeNotFoundError(pincode)
    return pincode_items[pincode]


@app.post("/pincode/bulk", response_model=BulkResponse, tags=["pincodes"])
def bulk_lookup(request: BulkRequest):
    results = [pincode_items[code] for code in request.pincodes if code in pincode_items]
    missing = [code for code in request.pincodes if code not in pincode_items]
    return BulkResponse(
        found=len(results),
        not_found=len(missing),
        missing=missing,
        results=results,
    )
