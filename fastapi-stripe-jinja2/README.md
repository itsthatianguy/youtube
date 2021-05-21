# Stripe Subscriptions with FastAPI and Jinja2

## Prerequisites
- Stripe account
- Stripe secret key set as an environment variable
- 2 subscription products created in Stripe
- Billing portal configured

## Getting started

Create a virtual environment for the project:  
`python3 -m venv virtualenv`

Then activate the virtual environment:  
`source virtualenv/bin/activate`  
Or on Powershell:  
`.\virtualenv\Scripts\Activate.ps1`

Enter your public key value, and price ids, in `static/script.js`  

Now install the dependencies for the project:  
`pip install -r requirements.txt`

You should now be able to run the API with:  
`python app.py`

In a browser navigate to `http://127.0.0.1:8000/`  
Create a premium or basic subscription  
This will create a customer in Stripe, and enable the billing portal  
