from fastapi import FastAPI, Request

app = FastAPI(
    title="Swiggy Order Service",
    description=(
        "Internal API for managing Orders"
        "Handle creation, tracking of delivery systems"
    ),
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

@app.get("/")
def hello_world():
    """Root endpoint - Health check"""
    return {"message": "Hello World"}

@app.get("/welcome")
def welcome():
    """Welcome endpoint - Welcome"""
    return {"message": "Welcome to the website"}

@app.get("/orders")
def get_orders():
    """Retrieve sample list of orders"""
    return {
        "orders": [
            {"order_id": "ORD-1001", "item": "Butter Chicken", "quantity": 1, "price": 350.0},
            {"order_id": "ORD-1002", "item": "Garlic Naan", "quantity": 2, "price": 80.0},
        ]
    }

@app.get("/orders/status")
def get_orders_status():
    """Retrieve sample order delivery status"""
    return {
        "order_id": "ORD-1001",
        "status": "In Transit",
        "estimated_delivery_minutes": 25,
        "driver_assigned": True,
    }

@app.get("/debug/request-info")
def get_orders_status(request: Request):
    """Inspect the raw request object"""
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "path_params": request.path_params,
        "query_params": dict(request.query_params)
    }

@app.get(
        "/orders/active", 
        summary="Get Active Orders", 
        description=(
            "Returns all orders that are currently being prepared" 
            "or are out for delivery"
        ), 
        tags=["orders"],
        response_description="List of active order objects",
        deprecated=False
        )
def get_active_orders():
    """This docstring also appreas in docs"""
    return {
        "active_orders": [
            {
                "order_id": "ORD-2001",
                "customer_name": "Aarav Sharma",
                "items": [
                    {"name": "Paneer Tikka", "quantity": 1, "price": 240.0},
                    {"name": "Butter Roti", "quantity": 3, "price": 45.0},
                ],
                "total_amount": 285.0,
                "status": "Preparing",
                "eta_minutes": 15,
            },
            {
                "order_id": "ORD-2002",
                "customer_name": "Priya Patel",
                "items": [
                    {"name": "Chicken Biryani", "quantity": 1, "price": 320.0},
                    {"name": "Raita", "quantity": 1, "price": 40.0},
                ],
                "total_amount": 360.0,
                "status": "Out for Delivery",
                "eta_minutes": 8,
            },
        ]
    }

@app.get("/resturants", tags=["Resturants"])
def list_restro():
    """Retrieve list of available restaurants"""
    return {
        "restaurants": [
            {
                "restaurant_id": "RST-101",
                "name": "Spice Garden",
                "cuisine": "North Indian",
                "rating": 4.5,
                "delivery_time_minutes": 30,
                "is_open": True,
            },
            {
                "restaurant_id": "RST-102",
                "name": "Dosa Plaza",
                "cuisine": "South Indian",
                "rating": 4.2,
                "delivery_time_minutes": 25,
                "is_open": True,
            },
            {
                "restaurant_id": "RST-103",
                "name": "Dragon Wok",
                "cuisine": "Chinese",
                "rating": 4.0,
                "delivery_time_minutes": 40,
                "is_open": False,
            },
        ]
    }
