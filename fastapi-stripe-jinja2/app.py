import os
import stripe
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

stripe.api_key = os.environ["STRIPE_KEY"]
# This is a terrible idea, only used for demo purposes!
app.state.stripe_customer_id = None


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "hasCustomer": app.state.stripe_customer_id is not None})


@app.get("/success")
async def success(request: Request):
    return templates.TemplateResponse("success.html", {"request": request})


@app.get("/cancel")
async def cancel(request: Request):
    return templates.TemplateResponse("cancel.html", {"request": request})


@app.post("/create-checkout-session")
async def create_checkout_session(request: Request):
    data = await request.json()

    if not app.state.stripe_customer_id:
        customer = stripe.Customer.create(
            description="Demo customer",
        )
        app.state.stripe_customer_id = customer["id"]

    checkout_session = stripe.checkout.Session.create(
        customer=app.state.stripe_customer_id,
        success_url="http://localhost:8000/success?session_id={CHECKOUT_SESSION_ID}",
        cancel_url="http://localhost:8000/cancel",
        payment_method_types=["card"],
        mode="subscription",
        line_items=[{
            "price": data["priceId"],
            "quantity": 1
        }],
    )
    return {"sessionId": checkout_session["id"]}


@app.post("/create-portal-session")
async def create_portal_session():
    session = stripe.billing_portal.Session.create(
        customer=app.state.stripe_customer_id,
        return_url="http://localhost:8000"
    )
    return {"url": session.url}


if __name__ == '__main__':
    uvicorn.run("app:app", reload=True)
